import json
import random
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.corpus import stopwords

# Load intents from intents.json
with open('intent.json') as file:
    intents = json.load(file)

def process_user_input(user_input):
    tokens = word_tokenize(user_input.lower())
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word.isalnum() and word not in stop_words]

    for intent in intents['intents']:
        for pattern in intent['patterns']:
            if all(token in tokens for token in word_tokenize(pattern.lower())):
                return intent['tag']

    return None


# Example usage
while True:
    user_input = input("user > ")
    if user_input == 'exit':
        break
    intent = process_user_input(user_input)

    if intent == 'add_task':
        print("User wants to add a task")
    elif intent == 'delete_task':
        print("User wants to delete a task")
    elif intent == 'modify_task':
        print("User wants to modify a task")
    else:
        print("Intent unknown")
