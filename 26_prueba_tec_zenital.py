import sqlite3
import os
import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt

# data = pd.read_sql('customer_courier_conversations.db')
# cargo los datos de las tablas
# Use a named path and validate it so failures are more actionable
db_path = (r"C:\SolucionesPT\comunicacion_mensajes_zenital.db")

import sqlite3
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import argparse


def _find_table(names, keywords):
    for k in keywords:
        for t in names:
            if k in t.lower():
                return t
    return None


def _create_sample_db(path: str):
    """Create a tiny sample DB with `messages` and `orders` tables for testing."""
    con = sqlite3.connect(path)
    cur = con.cursor()
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY,
            order_id INTEGER,
            sender_app_type TEXT,
            sender_role TEXT,
            message_sent_time TEXT,
            order_stage TEXT
        )
        """
    )
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS orders (
            order_id INTEGER PRIMARY KEY,
            city_code TEXT
        )
        """
    )
    # insert sample rows
    cur.execute("INSERT INTO orders(order_id, city_code) VALUES (1, 'LIM')")
    cur.execute(
        "INSERT INTO messages(order_id, sender_app_type, sender_role, message_sent_time, order_stage) VALUES (1, 'courier_app', 'Courier', '2025-11-20 10:00:00', 'delivered')"
    )
    cur.execute(
        "INSERT INTO messages(order_id, sender_app_type, sender_role, message_sent_time, order_stage) VALUES (1, 'customer_app', 'Customer', '2025-11-20 10:05:00', 'delivered')"
    )
    con.commit()
    con.close()


def process_db(db_path: str, messages_table: str = None, orders_table: str = None):
    """Load tables, compute metrics and return final dataframe.

    - db_path: path to sqlite file
    - messages_table / orders_table: optional explicit table names
    """
    if not os.path.exists(db_path):
        raise FileNotFoundError(f"SQLite DB file not found at '{db_path}'.\nCWD: {os.getcwd()}")

    if os.path.getsize(db_path) == 0:
        raise ValueError(f"DB file at '{db_path}' has size 0 bytes. Is this the correct file?")

    conn = sqlite3.connect(db_path)

    tables_df = pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table';", conn)
    table_list = tables_df['name'].astype(str).tolist()
    print("Detected tables:", table_list)

    # detect names if not supplied
    if messages_table is None:
        messages_table = _find_table(table_list, ['message', 'messages', 'msg', 'chat'])
    if orders_table is None:
        orders_table = _find_table(table_list, ['order', 'orders'])

    if messages_table is None or orders_table is None:
        file_size = None
        try:
            file_size = os.path.getsize(db_path)
        except Exception:
            pass
        raise ValueError(
            "Could not auto-detect 'messages' or 'orders' table. Detected tables: {}\n".format(table_list)
            + f"DB path: {db_path} (exists={os.path.exists(db_path)}, size={file_size})\n"
            + "You can supply table names with --messages-table and --orders-table when running the script."
        )

    print(f"Using messages table: {messages_table}, orders table: {orders_table}")

    messages = pd.read_sql_query(f"SELECT * FROM '{messages_table}'", conn)
    orders = pd.read_sql_query(f"SELECT * FROM '{orders_table}'", conn)

    # normalizar variables
    if 'sender_app_type' in messages.columns:
        messages['senders'] = np.where(
            messages['sender_app_type'].str.lower().str.contains('courier', na=False),
            'Courier',
            np.where(
                messages['sender_app_type'].str.lower().str.contains('customer', na=False),
                'Customer',
                'Unknown'
            )
        )
    else:
        messages['senders'] = 'Unknown'

    # hago el merge de las tablas, equivalente al LEFT JOIN en SQL
    if 'order_id' not in messages.columns:
        raise KeyError("'order_id' column not found in messages table")
    if 'order_id' not in orders.columns:
        raise KeyError("'order_id' column not found in orders table")

    # safe selection of city_code
    orders_sel = orders.copy()
    if 'city_code' not in orders_sel.columns:
        orders_sel['city_code'] = None

    base = messages.merge(
        orders_sel[['order_id', 'city_code']],
        on='order_id',
        how='left'
    )

    if 'message_sent_time' in base.columns:
        base['message_sent_time'] = pd.to_datetime(base['message_sent_time'])
    else:
        raise KeyError("'message_sent_time' column not found in messages/orders join result")

    first_msg = (
        base.groupby('order_id')['message_sent_time']
            .min()
            .reset_index(name='conversation_started_at')
    )

    first_msg_sender = (
        base.merge(first_msg, on='order_id')
            .query('message_sent_time == conversation_started_at')
            .loc[:, ['order_id', 'sender_role']]
            .rename(columns={'sender_role': 'first_message_by'})
    )

    last_msg = (
        base.groupby('order_id')['message_sent_time']
            .max()
            .reset_index(name='last_message_time')
    )

    last_msg_stage = (
        base.merge(last_msg, on=['order_id', 'message_sent_time'])
            .loc[:, ['order_id', 'order_stage']]
            .rename(columns={'order_stage': 'last_message_order_stage'})
    )

    courier_msgs = (
        base[base.get('sender_role') == 'Courier']
            .groupby('order_id')
            .agg(
                first_courier_message=('message_sent_time', 'min'),
                num_messages_courier=('message_sent_time', 'count')
            )
            .reset_index()
    )

    customer_msgs = (
        base[base.get('sender_role') == 'Customer']
            .groupby('order_id')
            .agg(
                first_customer_message=('message_sent_time', 'min'),
                num_messages_customer=('message_sent_time', 'count')
            )
            .reset_index()
    )

    response_df = (
        base.merge(first_msg, on='order_id')
            .merge(first_msg_sender, on='order_id')
    )

    response_messages = (
        response_df[
            (response_df['message_sent_time'] > response_df['conversation_started_at']) &
            (response_df['sender_role'] != response_df['first_message_by'])
        ]
    )

    first_response = (
        response_messages.groupby('order_id')['message_sent_time']
            .min()
            .reset_index(name='first_response_time')
    )

    # Calcular delay en segundos
    if not first_response.empty and 'first_response_time' in first_response.columns:
        first_response['first_responsetime_delay_seconds'] = (
            (first_response['first_response_time'] - first_msg['conversation_started_at'])
            .dt.total_seconds()
        )
    else:
        # create empty column if no responses
        first_response['first_responsetime_delay_seconds'] = pd.Series(dtype='float64')

    # dataframe (equivalente al INSERT final)
    df = (
        base[['order_id', 'city_code']]
            .drop_duplicates()
            .merge(first_msg, on='order_id', how='left')
            .merge(first_msg_sender, on='order_id', how='left')
            .merge(courier_msgs, on='order_id', how='left')
            .merge(customer_msgs, on='order_id', how='left')
            .merge(first_response[['order_id', 'first_responsetime_delay_seconds']], on='order_id', how='left')
            .merge(last_msg, on='order_id', how='left')
            .merge(last_msg_stage, on='order_id', how='left')
            .sort_values('order_id')
    )

    conn.close()
    return df


def main(argv=None):
    parser = argparse.ArgumentParser(description="Process communication DB and compute metrics.")
    parser.add_argument("--db", dest="db_path", default="comunicacion_mensajes_zenital.db",
                        help="Path to SQLite DB file (default: comunicacion_mensajes_zenital.db)")
    parser.add_argument("--messages-table", dest="messages_table", default=None,
                        help="Explicit messages table name (optional)")
    parser.add_argument("--orders-table", dest="orders_table", default=None,
                        help="Explicit orders table name (optional)")
    parser.add_argument("--create-sample", dest="create_sample", action="store_true",
                        help="If DB is missing or empty, create a small sample DB for testing")
    args = parser.parse_args(argv)

    db_path = args.db_path

    if not os.path.exists(db_path) or os.path.getsize(db_path) == 0:
        if args.create_sample:
            print(f"Creating sample DB at {db_path} for testing...")
            _create_sample_db(db_path)
        else:
            raise FileNotFoundError(
                f"SQLite DB file not found or empty at '{db_path}'.\n" \
                f"Current working directory: {os.getcwd()}\nFiles here: {os.listdir('.')[:50]}\n" \
                f"If you want to create a small test DB, re-run with --create-sample."
            )

    df = process_db(db_path, messages_table=args.messages_table, orders_table=args.orders_table)
    print(df.head())


if __name__ == '__main__':
    main()