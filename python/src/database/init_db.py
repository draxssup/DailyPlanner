import sqlite3

conn = sqlite3.connect('planner.db')
cur = conn.cursor()

# Create USER table
cur.execute('''CREATE TABLE IF NOT EXISTS USER (
               user_id INTEGER PRIMARY KEY,
               name VARCHAR(10),
               premium VARCHAR(3) CHECK (premium IN ('yes', 'no')),
               password VARCHAR(10))''')  # Removed the comma at the end

# Create CREATES table
cur.execute('''CREATE TABLE IF NOT EXISTS CREATES (
               user_id INTEGER,
               task_id INTEGER,
               PRIMARY KEY (user_id, task_id),
               FOREIGN KEY (user_id) REFERENCES USER(user_id),
               FOREIGN KEY (task_id) REFERENCES TASK(task_id))''')

# Create TASK table
cur.execute('''CREATE TABLE IF NOT EXISTS TASK (
               task_id INTEGER PRIMARY KEY,
               name VARCHAR(255),
               desc TEXT,
               date DATETIME,
               status VARCHAR(15))''')

conn.commit()
conn.close()
