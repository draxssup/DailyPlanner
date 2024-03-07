import sqlite3

conn = sqlite3.connect('../database/planner.db')
cur = conn.cursor()


def add_user(name: str, premium: str, age: int) -> None:
    cur.execute("INSERT INTO USER (name, premium, age) VALUES (?, ?, ?)", (name, premium, age))
    conn.commit()


def add_task(name:str , desc:str , start_time: str, end_time:str) -> None:
    cur.execute("INSERT INTO TASK (name, desc, start_time, end_time) VALUES (?, ?, ?, ?)",
                (name, desc, start_time, end_time))
    conn.commit()


def assign_task(user_id: int, task_id: int) -> None:
    cur.execute("INSERT INTO CREATES (user_id, task_id) VALUES (?, ?)", (user_id, task_id))
    conn.commit()


def display_tasks(user_id: int) -> None:
    cur.execute(
        '''SELECT TASK.name, TASK.desc, TASK.start_time, TASK.end_time FROM TASK 
        INNER JOIN CREATES ON TASK.task_id = CREATES.task_id WHERE CREATES.user_id = ?''', (user_id,))
    rows = cur.fetchall()
    columns = [column[0] for column in cur.description]
    for row in rows:
        for i in range(len(row)):
            print(f"{columns[i]}: {row[i]}")


def update_task(task_id: int, name=None, desc=None, start_time=None, end_time=None):
    if name:
        cur.execute("UPDATE TASK SET name = ? WHERE task_id = ?", (name, task_id))
    if desc:
        cur.execute("UPDATE TASK SET desc = ? WHERE task_id = ?", (desc, task_id))
    if start_time:
        cur.execute("UPDATE TASK SET start_time = ? WHERE task_id = ?", (start_time, task_id))
    if end_time:
        cur.execute("UPDATE TASK SET end_time = ? WHERE task_id = ?", (end_time, task_id))
    conn.commit()


def delete_task(task_id: int) -> None:
    cur.execute("DELETE FROM TASK WHERE task_id = ?", (task_id,))
    conn.commit()


def get_user_id(name: str) -> int:
    cur.execute("SELECT user_id FROM USER WHERE name = ?", (name,))
    user_id = cur.fetchone()[0]
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
