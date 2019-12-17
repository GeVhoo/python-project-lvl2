import json


# Open json file and return set
def get_set(path):
    dictionary = json.load(open(path))
    return set(dictionary.items())
