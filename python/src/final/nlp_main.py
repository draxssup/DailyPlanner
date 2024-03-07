import json
import sqlite3

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from DailyPlanner.python.src.final import alt_main as a
conn = sqlite3.connect('../database/planner.db')
cur = conn.cursor()
# Load intents from intents.json
with open('../../NLP/intent.json') as file:
    intents = json.load(file)


def process_user_input(user_input):
    tokens = word_tokenize(user_input.lower())
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word.isalnum() and word not in stop_words]

    for intent in intents['intents']:
        for pattern in intent['patterns']:
            if all(token in tokens for token in word_tokenize(pattern.lower())):
                return intent

    return None


# Example usage
user_name: str = a.greet()
print(user_name)
while True:
    user_input = input("user > ")
    if user_input == 'exit':
        break
    intent = process_user_input(user_input)

    if intent['tag'] == 'add_task':
        a.create_task(a.f.get_user_id(user_name))

    elif intent['tag'] == 'delete_task':
        a.delete_task()
    elif intent['tag'] == 'modify_task':
        print("User wants to modify a task")
    else:
        print("Please be more specific")
