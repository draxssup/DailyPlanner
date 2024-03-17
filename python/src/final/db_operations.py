import sqlite3
import re
import matplotlib.pyplot as plt

conn = sqlite3.connect('../database/planner.db')
cur = conn.cursor()


def add_user(name: str, age, premium='no',) -> None:
    cur.execute("INSERT INTO USER (name, premium, age) VALUES (?, ?, ?)", (name, premium, age))
    conn.commit()


def add_task(name: str, desc: str, date: str) -> None:
    cur.execute("INSERT INTO TASK (name, desc, date, status) VALUES (?, ?, ?, ?)",
                (name, desc, date, "ongoing"))
    conn.commit()


def assign_task(user_id: int, task_id: int) -> None:
    cur.execute("INSERT INTO CREATES (user_id, task_id) VALUES (?, ?)", (user_id, task_id))
    conn.commit()


def display_tasks(user_id: int) -> None:
    cur.execute(
        '''SELECT TASK.name, TASK.desc, TASK.date FROM TASK 
        INNER JOIN CREATES ON TASK.task_id = CREATES.task_id WHERE CREATES.user_id = ? and TASK.status not in ('completed')''', (user_id,))
    rows = cur.fetchall()
    columns = [column[0] for column in cur.description]
    print(f"Total {len(rows)} tasks:")
    for index, row in enumerate(rows, start=1):
        print(f"Task {index}:")
        for i in range(len(row)):
            print(f"{columns[i]}: {row[i]}")
        print()


def is_valid_date(input_string):
    pattern = r"^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])$"
    return re.match(pattern, input_string) is not None


def update_task(task_id: int, name=None, desc=None, date=None, status=None):
    if name:
        cur.execute("UPDATE TASK SET name = ? WHERE task_id = ?", (name, task_id))
    if desc:
        cur.execute("UPDATE TASK SET desc = ? WHERE task_id = ?", (desc, task_id))
    if date:
        cur.execute("UPDATE TASK SET date = ? WHERE task_id = ?", (date, task_id))
    if status:
        cur.execute("UPDATE TASK SET status = ? WHERE task_id = ?", (status, task_id))
    conn.commit()


def delete_task(task_id: int) -> None:
    cur.execute("DELETE FROM TASK WHERE task_id = ?", (task_id,))
    conn.commit()


def get_user_id(name: str) -> int:
    cur.execute("SELECT user_id FROM USER WHERE name = ?", (name,))
    try:
        user_id = cur.fetchone()[0]
    except Exception as e:
        user_id = None
    return user_id


def get_task_id(name: str) -> int:
    cur.execute("SELECT task_id FROM TASK WHERE name = ?", (name,))
    task_id = cur.fetchone()[0]
    return task_id


def clear_all_tasks() -> None:
    cur.execute("DELETE FROM TASK")
    conn.commit()
    print("All tasks cleared successfully!")


def clear_all_users() -> None:
    cur.execute("DELETE FROM USER")
    conn.commit()
    print("All tasks cleared successfully!")


def clear_all_assignments() -> None:
    cur.execute("DELETE FROM CREATES")
    conn.commit()
    print("All tasks cleared successfully!")
