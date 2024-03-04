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


def display_tasks(user_id: int) -> None:
    cur.execute(
        '''SELECT TASK.name, TASK.desc, TASK.start_time, TASK.end_time FROM TASK 
        INNER JOIN CREATES ON TASK.task_id = CREATES.task_id WHERE CREATES.user_id = ?''', (user_id,))
    rows = cur.fetchall()
    for row in rows:
        print(row)


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


def main() -> None:
    while True:
        print("\nOptions:")
        print("1. Create a new user")
        print("2. Continue with an existing user")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter new user's name: ")
            premium = input("Is the user premium (yes/no): ")
            age = int(input("Enter user's age: "))
            add_user(name, premium, age)
            print("User created successfully!")
            continue

        elif choice == '2':
            user_name = input("Enter user's name: ")
            user_id = get_user_id(user_name)
            if user_id is not None:
                print(f"Hello {user_name}!")
            else:
                print("User not found. Please try again.")
                continue

        elif choice == '3':
            break

        else:
            print("Invalid choice. Please try again.")
            continue

        while True:
            print("\nOptions:")
            print("1. Create a new task")
            print("2. Display tasks")
            print("3. Update a task")
            print("4. Delete a task")
            print("5. Exit")

            sub_choice = input("Enter your choice: ")

            if sub_choice == '1':
                name = input("Enter task name: ")
                desc = input("Enter task description: ")
                start_time = input("Enter start time (YYYY-MM-DD HH:MM:SS): ")
                end_time = input("Enter end time (YYYY-MM-DD HH:MM:SS): ")
                add_task(name, desc, start_time, end_time)
                assign_task(cur, user_id, cur.lastrowid)
                print("Task created successfully!")

            elif sub_choice == '2':  # display
                display_tasks(user_id)
            elif sub_choice == '3':  # update
                task_name = input("Enter task name to update: ")
                task_id = get_task_id(task_name)
                name = input("Enter new task name (leave blank to keep current): ")
                desc = input("Enter new task description (leave blank to keep current): ")
                start_time = input("Enter new start time (YYYY-MM-DD HH:MM:SS, leave blank to keep current): ")
                end_time = input("Enter new end time (YYYY-MM-DD HH:MM:SS, leave blank to keep current): ")
                update_task(task_id, name, desc, start_time, end_time)
                print("Task updated successfully!")

            elif sub_choice == '4':  # delete
                task_name = input("Enter name of the task to delete: ")
                delete_task(get_task_id(task_name))
                print("Task deleted successfully!")

            elif sub_choice == '5':
                break

            else:
                print("Invalid choice. Please try again.")
    conn.close()


if __name__ == "__main__":
    main()
