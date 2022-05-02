import json
import sqlite3
conn = sqlite3.connect("database/DB/db.sqlite3")
c = conn.cursor()


def read_json(filename):
    with open(f"./static/{filename}.json", 'r') as f:
        data = json.load(f)
        return data


def write_json(filename, data_set):
    with open(f"./static/{filename}.json", 'w') as f:
        json.dump(data_set, f, indent=4)


def create_table():

    pass
