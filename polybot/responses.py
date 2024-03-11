import json


def load_responses():
    with open('./responses.json', 'r') as file:
        return json.load(file)

