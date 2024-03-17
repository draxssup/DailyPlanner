import random
import tkinter as tk

user_name = user_id = None


def update_user_message_box(event=None):
    text = textb.get()
    if text:
        usr_msg.insert(tk.END, "User: " + text + "\n")
        usr_msg.yview(tk.END)


def update_ans_message_box(event=None):
    msg: str = check_intent_and_set_msg(nm.process_user_input(textb.get()))
    if textb.get():  # Check if the text is not empty
        # Add new message to the message display
        usr_msg.insert(tk.END, "DP: " + msg + "\n")
        textb.delete(0, tk.END)

        # Scroll to the bottom of the message display
        usr_msg.yview(tk.END)


def create_task(user_id):
    update_ans_message_box("Enter Task Name")
    textb.get()


def check_intent_and_set_msg(intent) -> str:
    if intent and intent['tag'] == 'add_task':
        create_task(a.f.get_user_id(user_name))
    elif intent and intent['tag'] == 'delete_task':
        delete_task()
    elif intent and intent['tag'] == 'modify_task':
        update_task()
    elif intent and intent['tag'] == 'complete_task':
        complete_task()
    elif intent and intent['tag'] == 'greetings':
        print(str(random.choice(intent['responses'])))
    elif intent and intent['tag'] == 'list_tasks':
        a.display_tasks(a.f.get_user_id(user_name))
    elif intent and intent['tag'] == 'help':
        print(random.choice(intent['responses']))
    elif intent and intent['tag'] == 'gratitude':
        print(random.choice(intent['responses']))
    else:
        print("Please be more specific")


def send_func(event=None):
    update_user_message_box()
    update_ans_message_box()


if __name__ == "__main__":
    import DailyPlanner.python.src.final.nlp_main as nm

root = tk.Tk()
font = ('Arial', 18)
root.geometry('900x900')
root.rowconfigure(0, weight=9)
root.rowconfigure(1, weight=1)

mf = tk.Frame(root)

usr_msg = tk.Text(mf, font=font, wrap="word", width=68)
usr_msg.grid(row=0, column=1, sticky='news')

mf.grid(row=0, column=0, sticky='news')
root.title("Task manager")

cf = tk.Frame(root)
textb = tk.Entry(cf, width=60, font=font)
cf.columnconfigure(0, weight=9)
cf.columnconfigure(1, weight=1)
textb.grid(row=0, column=0, padx=10, pady=10)
textb.bind("<Return>", send_func)  # Bind the Enter key to the update_message_box function

sendb = tk.Button(cf, height=2, font=font, text='Send', command=send_func)
sendb.grid(row=0, column=1)

cf.grid(row=1, column=0)

root.mainloop()
