import json


def load_responses():
    file_path = './responses.json'
    with open(file_path, 'r') as file:
        try:
            responses_data = json.load(file)
            return responses_data
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            return None
