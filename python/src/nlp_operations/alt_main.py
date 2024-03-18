from datetime import datetime, timedelta

import DailyPlanner.python.src.nlp_operations.db_operations as f


def greet():
    c = input("Would you like to Login or signup\nuser > ")
    if c.lower() == 'login':
        d = login_user()
        if d == "-1":
            greet()
        return d
    elif c.lower() == 'signup':
        d = create_user()
        if d == "-1":
            greet()
        return d
    else:
        print("Try again later")


def create_user():
    name = input("Enter new user's name: ")
    if name == 'exit':
        return "-1"
    password = int(input("Enter password: "))
    f.add_user(name, password)
    print("User created successfully!")
    return name


def login_user():
    user_name = input("Enter user's name: ")
    user_id = f.get_user_id(user_name)
    while user_id is None:
        if user_name == 'exit':
            return "-1"
        print("User not found. Please try again.")
        user_name = input("Enter user's name: ")
        user_id = f.get_user_id(user_name)
    print(f"Hello {user_name}!")
    return user_name


def create_task(user_id):
    name = input("Enter task name: ")
    desc = input("Enter task description: ")
    date = input("Enter Date (DD/MM): ")
    if date.lower() == "today":
        today = datetime.now()
        date = today.strftime("%d/%m")
    elif date.lower() == "tomorrow":
        tomorrow = datetime.today() + timedelta(days=1)
        date = tomorrow.strftime("%d/%m")
    while not f.is_valid_date(date):
        print("Wrong format try again")
        date = input("Enter Date (DD/MM):")
    f.add_task(name, desc, date)
    f.assign_task(user_id, f.cur.lastrowid)
    print("Task created successfully!")


def display_tasks(user_id):
    return f.display_tasks(user_id)


def update_task():
    task_name = input("Enter task name to update: ")
    task_id = f.get_task_id(task_name)
    name = input("Enter new task name (leave blank to keep current): ")
    desc = input("Enter new task description (leave blank to keep current): ")
    date = input("Enter new Date (leave blank to keep current): ")
    f.update_task(task_id, name, desc, date)
    print("Task updated successfully!")


def delete_task():
    task_name = input("Enter name of the task to delete: ")
    f.delete_task(f.get_task_id(task_name))
    print("Task deleted successfully!")


def complete_task():
    task_name = input("Enter name of the completed task: ")
    f.cur.execute('SELECT name FROM TASK WHERE name = ?', (task_name,))
    result = f.cur.fetchone()
    if result is None:
        print("Task not found. Please try again.")
    else:
        task_id = f.get_task_id(task_name)
        f.update_task(task_id, status='completed')
        print(f"Congratulations on completing {task_name}")
