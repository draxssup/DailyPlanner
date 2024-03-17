import json
import random
import sqlite3
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import DailyPlanner.python.src.final.alt_main as a
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

# user_name = None
# print("Welcome to my Daily planner")
# while user_name is None:
#     user_name: str = a.greet()

#while True:
#    user_input = input(f"{user_name} > ")
#    if user_input == 'bye':
#        break
#    intent = process_user_input(user_input)
#
#    if intent and intent['tag'] == 'add_task':
#        a.create_task(a.f.get_user_id(user_name))
#    elif intent and intent['tag'] == 'delete_task':
#        a.delete_task()
#    elif intent and intent['tag'] == 'modify_task':
#        a.update_task()
#    elif intent and intent['tag'] == 'complete_task':
#        a.complete_task()
#    elif intent and intent['tag'] == 'greetings':
#        print(random.choice(intent['responses']))
#    elif intent and intent['tag'] == 'list_tasks':
#        a.display_tasks(a.f.get_user_id(user_name))
#    elif intent and intent['tag'] == 'help':
#        print(random.choice(intent['responses']))
#    elif intent and intent['tag'] == 'gratitude':
#        print(random.choice(intent['responses']))
#    else:
#        print("Please be more specific")
#