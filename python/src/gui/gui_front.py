import tkinter as tk
import sqlite3
import DailyPlanner.python.src.nlp_operations.db_operations as f

global user_name
user_name = None


def open_login_window():
    login_window = tk.Toplevel(root)
    login_window.title("Login")
    login_window.geometry('1200x800')

    # Function to check username and password
    def check_login():
        global user_name
        user_name = username_entry.get()
        password = password_entry.get()

        # Connect to the database
        conn = sqlite3.connect("../database/planner.db")
        c = conn.cursor()

        # Check if username and password match
        c.execute("SELECT * FROM user WHERE name=? and password = ?", (user_name,password))
        result = c.fetchone()
        if result:
            print("Login successful")
            login_window.destroy()
            root.destroy()
        else:
            print("Login failed")

        # Close the database connection
        conn.close()

    login_window.columnconfigure(0, weight=4)
    login_window.columnconfigure(1, weight=6)
    login_window.rowconfigure(0, weight=1)
    login_window.rowconfigure(1, weight=1)
    login_window.rowconfigure(2, weight=1)
    tk.Label(login_window, text="Username:", font=('Arial', 24)).grid(row=0, column=0, sticky='e')
    username_entry = tk.Entry(login_window, font=('Arial', 24))
    username_entry.grid(row=0, column=1, sticky='w')
    tk.Label(login_window, text="Password:", font=('Arial', 24)).grid(row=1, column=0, sticky='e')
    password_entry = tk.Entry(login_window, show="*", font=('Arial', 24))
    password_entry.grid(row=1, column=1, sticky='w')
    tk.Button(login_window, text="Login", font=('Arial', 24), command=check_login).grid(row=2, column=1, sticky='nw')


def get_username():
    global user_name
    return user_name


def open_signup_window():
    signup_window = tk.Toplevel(root)
    signup_window.geometry('1200x800')
    signup_window.title('Signup')

    def do_signup():
        password = passwordtb.get()
        if not password.isnumeric():
            tk.Label(signup_window, text='Try Again', font=('Arial', 18), fg='red').grid(row=2, column=0, sticky='ne',
                                                                                         padx=25)

        name = nametb.get()
        f.add_user(name, password, 'yes')
        tk.Label(signup_window, text='Successful', font=('Arial', 18), fg='green').grid(row=2, column=0, sticky='ne',
                                                                                        padx=25)
        signup_window.after(500, signup_window.destroy())

    signup_window.columnconfigure(0, weight=1)
    signup_window.columnconfigure(1, weight=1)
    signup_window.rowconfigure(0, weight=1)
    signup_window.rowconfigure(1, weight=1)
    signup_window.rowconfigure(2, weight=1)
    tk.Label(signup_window, text='Name', font=('Arial', 24)).grid(row=0, column=0, sticky='se')
    tk.Label(signup_window, text='password', font=('Arial', 24)).grid(row=1, column=0, sticky='ne')
    nametb = tk.Entry(signup_window, width=20, font=('Arial', 24))
    nametb.grid(pady=10, row=0, column=1, sticky='sw', padx=25)
    passwordtb = tk.Entry(signup_window, show='*', width=20, font=('Arial', 24))
    passwordtb.grid(row=1, column=1, sticky='nw', padx=25)
    submit_button = tk.Button(signup_window, text='submit', font=('Arial', 24), command=do_signup)
    submit_button.grid(row=2, column=1, sticky='nw')


root = tk.Tk()
root.geometry('1200x800')
root.title("Daily Planner")
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.rowconfigure(1, weight=1)
tk.Label(text='Welcome to Daily Planner\nHere you can create your tasks and manage them.', font=('Arial', 32)).grid(
    row=0, column=0, columnspan=2)
loginbut = tk.Button(root, text='LOGIN', font=('Arial', 24), command=open_login_window)
loginbut.grid(row=1, column=0)
signupbut = tk.Button(root, text='SIGNUP', font=('Arial', 24), command=open_signup_window)
signupbut.grid(row=1, column=1)

root.mainloop()
