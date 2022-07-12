import json

filepath = r'data_for_all_zones1.json'


def reading_json_file(path):
    with open(path, 'r') as file:
        dict_from_file = json.load(file)
        return dict_from_file
