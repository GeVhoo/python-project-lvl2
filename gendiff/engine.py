import os
import json
import yaml


def get_extension(file_path):
    return os.path.splitext(file_path)[-1]


# Open file and return set
def get_set(file_path):
    if get_extension(file_path) == 'yaml' or 'yml':
        return yaml.load(open(file_path), Loader=yaml.Loader)
    elif get_extension(file_path) == 'json':
        return json.load(open(file_path))
