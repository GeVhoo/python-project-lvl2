import json


def json_diff(dictionary):
    return json.dumps(dictionary, sort_keys=True, indent=4)
