from gendiff.constants import (IN_BEFORE, IN_AFTER, SAME, CHANGED, CHILDREN,
                               CONDITION, VALUE, BEFORE_VALUE, AFTER_VALUE)


def get_diff(before, after):
    # Get keys for both files
    before_keys_set = before.keys()
    after_keys_set = after.keys()
    # Get the keys difference in files
    keys_in_both = (before_keys_set & after_keys_set)
    keys_in_before = (before_keys_set - after_keys_set)
    keys_in_after = (after_keys_set - before_keys_set)
    # Get a dictionary with data on changes in both files
    result = {}
    for key in keys_in_before:
        result[key] = {
            CONDITION: IN_BEFORE,
            VALUE: get_value(before[key]),
            }
    for key in keys_in_after:
        result[key] = {
            CONDITION: IN_AFTER,
            VALUE: get_value(after[key]),
            }
    for key in keys_in_both:
        before_value = before[key]
        after_value = after[key]
        if before_value == after_value:
            result[key] = {
                CONDITION: SAME,
                VALUE: get_value(before_value),
                }
        elif isinstance(before_value, dict) and isinstance(after_value, dict):
            result[key] = {
                CONDITION: CHILDREN,
                VALUE: get_diff(before_value, after_value),
                }
        else:
            result[key] = {
                CONDITION: CHANGED,
                BEFORE_VALUE: get_value(before_value),
                AFTER_VALUE: get_value(after_value),
                }
    return result


def get_value(data):
    if type(data) is dict:
        for k, v in data.items():
            data[k] = get_str_value(v)
            return data
    else:
        return get_str_value(data)


def get_str_value(item):
    if type(item) is bool:
        return str(item).lower()
    else:
        return str(item)
