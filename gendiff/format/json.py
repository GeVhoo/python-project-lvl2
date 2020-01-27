import json


def format(dictionary):
    return json.dumps(dictionary, sort_keys=True, indent=4)
