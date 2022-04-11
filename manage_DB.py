import json


def read_json(filename):
    with open(f"{filename}.json", 'r') as f:
        data = json.load(f)
        return data


def write_json(filename, data_set):
    with open(f"{filename}.json", 'w') as f:
        json.dump(data_set, f, indent=4)
