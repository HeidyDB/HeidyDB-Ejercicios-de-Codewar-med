import sqlite3
import os
import pandas as pd
import sys

DB = 'comunicacion_mensajes_zenital.db'

if len(sys.argv) > 1:
    DB = sys.argv[1]

print('Checking DB path:', DB)
if not os.path.exists(DB):
    print('ERROR: file does not exist at this path')
    sys.exit(2)

size = os.path.getsize(DB)
print('File size (bytes):', size)

if size == 0:
    print('File is empty (0 bytes). This is not a valid SQLite DB file.')
    sys.exit(3)

con = sqlite3.connect(DB)
cur = con.cursor()
cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
rows = cur.fetchall()
if not rows:
    print('No tables found in DB')
    con.close()
    sys.exit(4)

tables = [r[0] for r in rows]
print('Tables found:', tables)

# show a small preview for each table
for t in tables:
    try:
        df = pd.read_sql_query(f"SELECT * FROM '{t}' LIMIT 5", con)
        print('\n--- Preview of table:', t, '---')
        print(df)
    except Exception as e:
        print(f'Could not read table {t}:', e)

con.close()
print('\nDone')
