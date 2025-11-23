
import sqlite3
import pandas as pd

# Ruta corregida
conn = sqlite3.connect("C:/SolucionesPT/comunicacion_mensajes_zenital.db")

query = """
WITH base AS (
    SELECT
        m.order_id,
        m.message_sent_time,
        m.sender_app_type,
        m.order_stage,
        o.city_code
    FROM customer_courier_chat_messages m
    LEFT JOIN orders o ON m.order_id = o.order_id
),

first_msg AS (
    SELECT 
        order_id,
        MIN(message_sent_time) AS conversation_started_at
    FROM base
    GROUP BY order_id
),

first_msg_sender AS (
    SELECT 
        b.order_id,
        b.sender_app_type AS first_message_by
    FROM base b
    JOIN first_msg fm
        ON b.order_id = fm.order_id
        AND b.message_sent_time = fm.conversation_started_at
),

last_msg AS (
    SELECT 
        order_id,
        MAX(message_sent_time) AS last_message_time
    FROM base
    GROUP BY order_id
),

last_stage AS (
    SELECT
        b.order_id,
        b.order_stage AS last_message_order_stage
    FROM base b
    JOIN last_msg lm
        ON b.order_id = lm.order_id
        AND b.message_sent_time = lm.last_message_time
),

courier_msgs AS (
    SELECT
        order_id,
        MIN(message_sent_time) AS first_courier_message,
        COUNT(*) AS num_messages_courier
    FROM base
    WHERE sender_app_type LIKE 'Courier%'
    GROUP BY order_id
),

customer_msgs AS (
    SELECT
        order_id,
        MIN(message_sent_time) AS first_customer_message,
        COUNT(*) AS num_messages_customer
    FROM base
    WHERE sender_app_type LIKE 'Customer%'
    GROUP BY order_id
),

response AS (
    SELECT
        fm.order_id,
        MIN(b.message_sent_time) AS first_response_time
    FROM first_msg fm
    JOIN first_msg_sender s 
        ON fm.order_id = s.order_id
    JOIN base b
        ON b.order_id = fm.order_id
        AND b.message_sent_time > fm.conversation_started_at
        AND b.sender_app_type <> s.first_message_by
    GROUP BY fm.order_id
)

SELECT
    b.order_id,
    b.city_code,
    c.first_courier_message,
    cu.first_customer_message,
    c.num_messages_courier,
    cu.num_messages_customer,
    fms.first_message_by,
    fm.conversation_started_at,
    CASE
        WHEN r.first_response_time IS NULL THEN NULL
        ELSE strftime('%s', r.first_response_time) - strftime('%s', fm.conversation_started_at)
    END AS first_responsetime_delay_seconds,
    lm.last_message_time,
    ls.last_message_order_stage
FROM (SELECT DISTINCT order_id, city_code FROM base) b
LEFT JOIN first_msg fm           ON b.order_id = fm.order_id
LEFT JOIN first_msg_sender fms   ON b.order_id = fms.order_id
LEFT JOIN last_msg lm            ON b.order_id = lm.order_id
LEFT JOIN last_stage ls          ON b.order_id = ls.order_id
LEFT JOIN courier_msgs c         ON b.order_id = c.order_id
LEFT JOIN customer_msgs cu       ON b.order_id = cu.order_id
LEFT JOIN response r             ON b.order_id = r.order_id
"""

df = pd.read_sql(query, conn)

print(df.head())
conn.close()



