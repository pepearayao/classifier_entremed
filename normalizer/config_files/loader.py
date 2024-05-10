import json
import os

def load_config_file(file_name):
    with open(os.path.join(os.path.dirname(__file__), f"{file_name}.json")) as f:
        d = json.load(f)
        return d
