import funct as f


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
            f.add_user(name, premium, age)
            print("User created successfully!")
            continue

        elif choice == '2':
            user_name = input("Enter user's name: ")
            user_id = f.get_user_id(user_name)
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
            print("5. Log Out")

            sub_choice = input("Enter your choice: ")

            if sub_choice == '1':
                name = input("Enter task name: ")
                desc = input("Enter task description: ")
                start_time = input("Enter start time (YYYY-MM-DD HH:MM:SS): ")
                end_time = input("Enter end time (YYYY-MM-DD HH:MM:SS): ")
                f.add_task(name, desc, start_time, end_time)
                f.assign_task(user_id, cur.lastrowid)
                print("Task created successfully!")

            elif sub_choice == '2':  # display
                f.display_tasks(user_id)
            elif sub_choice == '3':  # update
                task_name = input("Enter task name to update: ")
                task_id = f.get_task_id(task_name)
                name = input("Enter new task name (leave blank to keep current): ")
                desc = input("Enter new task description (leave blank to keep current): ")
                start_time = input("Enter new start time (YYYY-MM-DD HH:MM:SS, leave blank to keep current): ")
                end_time = input("Enter new end time (YYYY-MM-DD HH:MM:SS, leave blank to keep current): ")
                f.update_task(task_id, name, desc, start_time, end_time)
                print("Task updated successfully!")

            elif sub_choice == '4':  # delete
                task_name = input("Enter name of the task to delete: ")
                f.delete_task(get_task_id(task_name))
                print("Task deleted successfully!")

            elif sub_choice == '5':
                break

            else:
                print("Invalid choice. Please try again.")
    f.conn.close()


if __name__ == "__main__":
    main()