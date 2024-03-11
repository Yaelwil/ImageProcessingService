import json


def load_responses():
    with open('polybot/responses.json', 'r') as file:
        return json.load(file)

