from gendiff.constants import (IN_BEFORE, IN_AFTER, SAME, CHANGED, CHILDREN,
                               CONDITION, VALUE)


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
            VALUE: before[key],
            }
    for key in keys_in_after:
        result[key] = {
            CONDITION: IN_AFTER,
            VALUE: after[key],
            }
    for key in keys_in_both:
        before_value = before[key]
        after_value = after[key]
        if before_value == after_value:
            result[key] = {
                CONDITION: SAME,
                VALUE: before_value,
                }
        elif isinstance(before_value, dict) and isinstance(after_value, dict):
            result[key] = {
                CONDITION: CHILDREN,
                VALUE: get_diff(before_value, after_value),
                }
        else:
            result[key] = {
                CONDITION: CHANGED,
                VALUE: (before_value, after_value)
                }
    return result
