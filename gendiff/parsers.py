import os
import json
import yaml


# Open file and return set
def get_set(file_path):
    extension = os.path.splitext(file_path)[-1]
    if extension in ('.yaml', '.yml'):
        return yaml.load(open(file_path), Loader=yaml.SafeLoader)
    elif extension == '.json':
        return json.load(open(file_path))
