import tkinter as tk
import DailyPlanner.python.src.nlp_operations.db_operations as f
import DailyPlanner.python.src.gui.gui_front as g

username = g.get_username()
print(username)

# ROOT DEFINITION

# ============================================================
root = tk.Tk()
root.geometry('1600x2400')
root.columnconfigure(0, weight=6)
root.columnconfigure(1, weight=4)
# ============================================================

# VIEW FRAME DISPLAYS TASK

# ============================================================
view_frame = tk.Frame(root)
vfm = tk.Text(view_frame, font=('Arial', 24))
if vfm.get('1.0', 'end-1c'):
    vfm.delete(1.0, tk.END)
vfm.insert(1.0, f.display_tasks(user_id=f.get_user_id(username)))
vfm.pack(padx=5, pady=6, fill='x')
view_frame.grid(row=0, column=0, sticky='news')


# ============================================================

# CREATE BUTTON'S SLAVE LAYER TOPLEVEL + ROOT

# ============================================================

def create_create_layer():
    def submit_task():
        # Process the task creation (e.g., add to database)
        print('command working')
        name = name_entry.get()
        desc = desc_entry.get()
        date = date_entry.get()
        user_id = f.get_user_id(username)

        # Clear the view frame
        vfm.delete('1.0', tk.END)

        # Insert the new task and assign it to the user
        f.add_task(name, desc, date)
        task_id = f.get_task_id(name)
        try:
            f.assign_task(user_id, task_id)
        finally:
            print()
            vfm.delete('1.0', tk.END)
            vfm.insert('1.0', f.display_tasks(user_id=user_id))
            create_layer.destroy()

    create_layer = tk.Toplevel(root)
    create_layer.title('Create New Task')
    create_layer.geometry('1200x800')

    create_layer.columnconfigure(0, weight=3)
    create_layer.columnconfigure(1, weight=7)
    create_layer.rowconfigure(0, weight=1)
    create_layer.rowconfigure(1, weight=1)
    create_layer.rowconfigure(2, weight=1)
    create_layer.rowconfigure(3, weight=1)

    # Name Entry
    tk.Label(create_layer, text='Name:', font=('Arial', 24)).grid(row=0, column=0, sticky='w')
    name_entry = tk.Entry(create_layer, font=('Arial', 24), width=45)
    name_entry.grid(row=0, column=1, sticky='w')

    # Description Entry
    tk.Label(create_layer, text='Description:', font=('Arial', 24)).grid(row=1, column=0, sticky='w')
    desc_entry = tk.Entry(create_layer, width=45, font=('Arial', 24))
    desc_entry.grid(row=1, column=1, sticky='w')

    # Date Entry
    tk.Label(create_layer, text='Date (DD/MM):', font=('Arial', 24)).grid(row=2, column=0, sticky='w')
    date_entry = tk.Entry(create_layer, font=('Arial', 24), width=45)
    date_entry.grid(row=2, column=1, sticky='w')

    # Button to Submit
    submit_button = tk.Button(create_layer, text='Submit', font=('Arial', 24), command=submit_task)
    submit_button.grid(row=3, column=0, columnspan=2)


# ============================================================

# DELETE BUTTON'S SLAVE LAYER TOPLEVEL + ROOT

# ============================================================
def create_delete_layer():
    def delete_task(task_name):
        # Process the task deletion (e.g., remove from database)
        f.delete_task(f.get_task_id(task_name))
        user_id = f.get_user_id(username)
        vfm.delete(1.0, tk.END)
        vfm.insert(1.0, f.display_tasks(user_id=user_id))
        delete_layer.destroy()

    delete_layer = tk.Toplevel(root)
    delete_layer.title('Complete Task')
    delete_layer.geometry('1200x800')

    delete_layer.columnconfigure(0, weight=1)
    delete_layer.columnconfigure(1, weight=3)
    delete_layer.rowconfigure(0, weight=1)
    delete_layer.rowconfigure(1, weight=1)

    # Task ID Entry
    tk.Label(delete_layer, text='Task Name:', font=('Arial', 24)).grid(row=0, column=0, sticky='w')
    task_name_entry = tk.Entry(delete_layer, font=('Arial', 24), width=45)
    task_name_entry.grid(row=0, column=1, sticky='w')

    # Button to Delete
    del_button = tk.Button(delete_layer, text='Complete Task', font=('Arial', 24),
                           command=lambda: delete_task(task_name_entry.get()))
    del_button.grid(row=1, column=0, columnspan=2)


# ============================================================

# EDIT BUTTON'S SLAVE LAYER TOPLEVEL + ROOT

# ============================================================
def create_edit_layer():
    def submit_edit():
        # Process the task edit (e.g., update database)
        print('Edit command working')
        task_name = name_entry.get()
        new_name = new_name_entry.get()
        new_desc = new_desc_entry.get()
        new_date = new_date_entry.get()
        user_id = f.get_user_id(username)

        # Clear the view frame
        vfm.delete('1.0', tk.END)

        # Update the task details
        task_id = f.get_task_id(task_name)
        if task_id:
            if new_name:
                f.update_task(task_id, name=new_name)
            if new_desc:
                f.update_task(task_id, desc=new_desc)
            if new_date:
                f.update_task(task_id, date=new_date)

        # Display updated tasks
        vfm.insert('1.0', f.display_tasks(user_id=user_id))
        print('Edit done')
        edit_layer.destroy()

    edit_layer = tk.Toplevel(root)
    edit_layer.title('Edit Task')
    edit_layer.geometry('1200x800')

    edit_layer.columnconfigure(0, weight=3)
    edit_layer.columnconfigure(1, weight=7)
    edit_layer.rowconfigure(0, weight=1)
    edit_layer.rowconfigure(1, weight=1)
    edit_layer.rowconfigure(2, weight=1)

    # Task Name Entry
    tk.Label(edit_layer, text='Task Name:', font=('Arial', 24)).grid(row=0, column=0, sticky='w')
    name_entry = tk.Entry(edit_layer, font=('Arial', 24), width=45)
    name_entry.grid(row=0, column=1, sticky='w')

    # New Name Entry
    tk.Label(edit_layer, text='New Name:', font=('Arial', 24)).grid(row=1, column=0, sticky='w')
    new_name_entry = tk.Entry(edit_layer, font=('Arial', 24), width=45)
    new_name_entry.grid(row=1, column=1, sticky='w')

    # New Description Entry
    tk.Label(edit_layer, text='New Description:', font=('Arial', 24)).grid(row=2, column=0, sticky='w')
    new_desc_entry = tk.Entry(edit_layer, width=45, font=('Arial', 24))
    new_desc_entry.grid(row=2, column=1, sticky='w')

    # New Date Entry
    tk.Label(edit_layer, text='New Date (DD/MM):', font=('Arial', 24)).grid(row=3, column=0, sticky='w')
    new_date_entry = tk.Entry(edit_layer, font=('Arial', 24), width=45)
    new_date_entry.grid(row=3, column=1, sticky='w')

    # Button to Submit
    submit_button = tk.Button(edit_layer, text='Submit', font=('Arial', 24), command=submit_edit)
    submit_button.grid(row=4, column=0, columnspan=2)


# ============================================================

# BUTTON GRID FRAME SHOWS BUTTONS TO USER

# ============================================================
button_frame = tk.Frame(root)
button_frame.rowconfigure(0, weight=1)
button_frame.rowconfigure(1, weight=1)
button_frame.rowconfigure(2, weight=1)
button_frame.rowconfigure(3, weight=1)
create_button = tk.Button(button_frame, text='CREATE', font=('Arial', 24), width=15, command=create_create_layer)
delete_button = tk.Button(button_frame, text='COMPLETE', font=('Arial', 24), width=15, command=create_delete_layer)
edit_button = tk.Button(button_frame, text='EDIT', font=('Arial', 24), width=15, command=create_edit_layer)
create_button.grid(row=0, column=0, sticky='news', padx=100)
delete_button.grid(row=1, column=0, sticky='news', padx=100)
edit_button.grid(row=2, column=0, sticky='news', padx=100)
button_frame.grid(row=0, column=1, sticky='news')
# ============================================================


root.mainloop()
