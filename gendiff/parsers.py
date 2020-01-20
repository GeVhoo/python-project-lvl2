import os
import json
import yaml


# Open file and return set
def get_set(file_path):
    extension = os.path.splitext(file_path)[-1]
    if extension == 'yaml' or 'yml':
        return yaml.load(open(file_path), Loader=yaml.Loader)
    elif extension == 'json':
        return json.load(open(file_path))
