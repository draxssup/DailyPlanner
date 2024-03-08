import db_operations as f
import alt_main as a


def main() -> None:
    while True:
        print("\nOptions:")
        print("1. Create a new user")
        print("2. Continue with an existing user")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            user_name = a.create_user()
            continue

        elif choice == '2':
            user_name = a.login_user()

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
            print("5. Mark a task as completed")
            print("6. Log Out")

            sub_choice = input("Enter your choice: ")

            if sub_choice == '1':    # create
                a.create_task(f.get_user_id(user_name))
            elif sub_choice == '2':  # read
                f.display_tasks(f.get_user_id(user_name))
            elif sub_choice == '3':  # update
                a.update_task()
            elif sub_choice == '4':  # delete
                a.delete_task()
            elif sub_choice == '5':
                a.complete_task()
            elif sub_choice == '6':
                break
            else:
                print("Invalid choice. Please try again.")
    f.conn.close()


if __name__ == "__main__":
    main()
