import json
import os


def load_schema(dir_name, file_name):
    root_dir = os.path.dirname(__file__)

    path = os.path.join(root_dir, 'json_schemes', dir_name, file_name)

    with open(path) as file:
        json_schema = json.loads(file.read())

    return json_schema
