# This file is a test file to make initial timetable it takes input from user to make a manual timetable.

import json
from datetime import datetime


def create_task(date, start_time, end_time, name, description):
    return {
        'date': date,
        'start_time': start_time,
        'end_time': end_time,
        'name': name,
        'description': description
    }


def save_task(task):
    try:
        with open('timetable.json', 'r') as file:
            timetable = json.load(file)
    except FileNotFoundError:
        timetable = []

    timetable.append(task)

    with open('timetable.json', 'w') as file:
        json.dump(timetable, file, indent=4)


def view_timetable():
    try:
        with open('timetable.json', 'r') as file:
            timetable = json.load(file)
            for task in timetable:
                print(f"Date: {task['date']}")
                print(f"Start Time: {task['start_time']}")
                print(f"End Time: {task['end_time']}")
                print(f"Name: {task['name']}")
                print(f"Description: {task['description']}")
                print("\n")
    except FileNotFoundError:
        print("Timetable is empty.")


def main():
    while True:
        print("1. Create Task")
        print("2. View All Tasks")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            date = datetime.now().strftime('%Y-%m-%d')
            start_time = input("Enter start time (HH:MM): ")
            end_time = input("Enter end time (HH:MM): ")
            name = input("Enter name of the task: ")
            description = input("Enter description of the task: ")
            task = create_task(date, start_time, end_time, name, description)
            save_task(task)
            print("Task created successfully.")
        elif choice == '2':
            view_timetable()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

    print("Exiting program.")


if __name__ == "__main__":
    main()
