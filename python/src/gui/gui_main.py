import random
import tkinter as tk
import DailyPlanner.python.src.final.db_operations as f
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
output = 'wolow'
view_frame = tk.Frame(root)
vfm = tk.Text(view_frame, font=('Arial', 24))
if vfm.get('1.0', 'end-1c'):
    vfm.delete(1.0, tk.END)
vfm.insert(1.0, output)
vfm.pack(padx=5, pady=6, fill='x')
view_frame.grid(row=0, column=0, sticky='news')


# ============================================================
# CREATE BUTTON'S SLAVE LAYER TOPLEVEL + ROOT
def create_create_layer(event=None):
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
    submit_button = tk.Button(create_layer, text='Submit', font=('Arial', 24),
                              command=lambda: submit_task(name_entry.get(), desc_entry.get(), date_entry.get()))
    submit_button.grid(row=3, column=0, columnspan=2)


def submit_task(name, desc, date):
    # Process the task creation (e.g., add to database)
    user_id = f.get_user_id(username)
    f.add_task(name, desc, date)
    f.assign_task(f.get_task_id(name), user_id)


# BUTTON GRID FRAME SHOWS BUTTONS TO USER

# ============================================================
button_frame = tk.Frame(root)
button_frame.rowconfigure(0, weight=1)
button_frame.rowconfigure(1, weight=1)
button_frame.rowconfigure(2, weight=1)
button_frame.rowconfigure(3, weight=1)
create_button = tk.Button(button_frame, text='CREATE', font=('Arial', 24), width=15, command=create_create_layer)
delete_button = tk.Button(button_frame, text='DELETE', font=('Arial', 24), width=15)
edit_button = tk.Button(button_frame, text='EDIT', font=('Arial', 24), width=15)
complete_button = tk.Button(button_frame, text='COMPLETE', font=('Arial', 24), width=15)
create_button.grid(row=0, column=0, sticky='news', padx=100)
delete_button.grid(row=1, column=0, sticky='news', padx=100)
edit_button.grid(row=2, column=0, sticky='news', padx=100)
complete_button.grid(row=3, column=0, sticky='news', padx=100)
button_frame.grid(row=0, column=1, sticky='news')
# ============================================================


root.mainloop()
