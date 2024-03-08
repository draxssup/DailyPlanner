import sqlite3
conn = sqlite3.connect('planner.db')
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS creates; ")
cur.execute("DROP TABLE IF EXISTS task; ")
cur.execute("DROP TABLE IF EXISTS user; ")
