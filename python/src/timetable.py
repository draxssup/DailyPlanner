# This file is a test file to make initial timetable it takes input from user to make a manual timetable.

import json


def create_timetable():
    timetable = []
    while True:
        date = input("Enter date (YYYY-MM-DD) or type 'done' to exit: ")
        if date.lower() == 'done':
            break
        start_time = input("Enter start time (HH:MM): ")
        end_time = input("Enter end time (HH:MM): ")
        name = input("Enter name of the task: ")
        description = input("Enter description of the task: ")
        timetable.append({
            'date': date,
            'start_time': start_time,
            'end_time': end_time,
            'name': name,
            'description': description
        })
        return timetable


def save_timetable(timetable):
    with open('timetable.json', 'w') as file:
        json.dump(timetable, file, indent=4)


def main():
    timetable = create_timetable()
    save_timetable(timetable)
    print("Timetable saved to 'timetable.json'.")


if __name__ == "__main__":
    main()
