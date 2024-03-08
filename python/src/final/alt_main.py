from DailyPlanner.python.src.final import funct as f


def greet():
    c = int(input("Welcome to my Daily planner\nEnter 1. to login\nEnter 2. to signup: "))
    if c == 1:
        return login_user()
    elif c == 2:
        return create_user()
    else:
        print("Try again later")


def create_user():
    name = input("Enter new user's name: ")
    premium = input("Is the user premium (yes/no): ")
    age = int(input("Enter user's age: "))
    f.add_user(name, premium, age)
    print("User created successfully!")
    return name


def login_user():
    user_name = input("Enter user's name: ")
    user_id = f.get_user_id(user_name)
    if user_id is not None:
        print(f"Hello {user_name}!")
        return user_name
    else:
        print("User not found. Please try again.")


def create_task(user_id):
    name = input("Enter task name: ")
    desc = input("Enter task description: ")
    date = input("Enter Date : ")
    f.add_task(name, desc, date)
    f.assign_task(user_id, f.cur.lastrowid)
    print("Task created successfully!")


def display_tasks(user_id):
    f.display_tasks(user_id)


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
