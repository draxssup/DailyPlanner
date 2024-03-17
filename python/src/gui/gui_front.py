import os
import tkinter as tk
import sqlite3
import DailyPlanner.python.src.nlp_operations.db_operations as f

global user_name
user_name = None


def open_login_window():
    login_window = tk.Toplevel(root)
    login_window.title("Login")
    login_window.geometry('200x200')

    # Function to check username and password
    def check_login():
        global user_name
        user_name = username_entry.get()

        # Connect to the database
        conn = sqlite3.connect("../database/planner.db")
        c = conn.cursor()

        # Check if username and password match
        c.execute("SELECT * FROM user WHERE name=?", (user_name,))
        result = c.fetchone()
        if result:
            print("Login successful")
            login_window.destroy()
            root.destroy()
        else:
            print("Login failed")

        # Close the database connection
        conn.close()

    username_label = tk.Label(login_window, text="Username:", font=('Arial', 18))
    username_label.pack()
    username_entry = tk.Entry(login_window, font=('Arial', 18))
    username_entry.pack()
    password_label = tk.Label(login_window, text="Password:", font=('Arial', 18))
    password_label.pack()
    password_entry = tk.Entry(login_window, show="*", font=('Arial', 18))
    password_entry.pack()
    login_button = tk.Button(login_window, text="Login", font=('Arial', 18), command=check_login)
    login_button.pack(fill='x')


def get_username():
    global user_name
    return user_name


def open_signup_window():
    signup_window = tk.Toplevel(root)
    signup_window.geometry('300x300')
    signup_window.title('Signup')

    def do_signup():
        age = agetb.get()
        if not age.isnumeric():
            tk.Label(signup_window, text='Try Again', font=('Arial', 12), fg='red').grid(row=2, column=0)

        name = nametb.get()
        f.add_user(name, age, 'yes')
        tk.Label(signup_window, text='Successful', font=('Arial', 12), fg='green').grid(row=2, column=0)
        signup_window.after(500, signup_window.destroy())

    signup_window.columnconfigure(0, weight=1)
    signup_window.columnconfigure(1, weight=9)
    signup_window.rowconfigure(0, weight=1)
    signup_window.rowconfigure(1, weight=1)
    tk.Label(signup_window, text='Name', font=('Arial', 18)).grid(pady=10, row=0, column=0, sticky='nw')
    tk.Label(signup_window, text='Age', font=('Arial', 18)).grid(row=1, column=0, sticky='nw')
    nametb = tk.Entry(signup_window, width=20, font=('Arial', 18))
    nametb.grid(pady=10, row=0, column=1, sticky='new')
    agetb = tk.Entry(signup_window, width=20, font=('Arial', 18))
    agetb.grid(row=1, column=1, sticky='new')
    submit_button = tk.Button(signup_window, text='submit', font=('Arial', 18), command=do_signup)
    submit_button.grid(sticky='news', row=2, column=1)


root = tk.Tk()
root.geometry('500x500')
root.title("Daily Planner")
loginbut = tk.Button(root, text='LOGIN', font=('Arial', 18), command=open_login_window)
loginbut.pack(pady=25, fill='x')
signupbut = tk.Button(root, text='SIGNUP', font=('Arial', 18), command=open_signup_window)
signupbut.pack(fill='x')

root.mainloop()
