import json


def output(dictionary):
    return json.dumps(dictionary, sort_keys=True, indent=4)
