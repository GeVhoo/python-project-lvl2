from gendiff.constants import IN_BEFORE, IN_AFTER, SAME, CHANGED, CHILDREN


def get_diff(before, after):
    # Get keys for both files
    before_keys_set = set(before.keys())
    after_keys_set = set(after.keys())
    # Get the keys difference in files
    keys_in_both = (before_keys_set & after_keys_set)
    keys_in_before = (before_keys_set - after_keys_set)
    keys_in_after = (after_keys_set - before_keys_set)
    # Get a dictionary with data on changes in both files
    result = {}
    for key in keys_in_before:
        result[key] = {
            'condition': IN_BEFORE,
            'value': before[key],
            }
    for key in keys_in_after:
        result[key] = {
            'condition': IN_AFTER,
            'value': after[key],
            }
    for key in keys_in_both:
        if before[key] == after[key]:
            result[key] = {
                'condition': SAME,
                'value': before[key],
                }
        elif type(before[key]) is dict and type(after[key]) is dict:
            result[key] = {
                'condition': CHILDREN,
                'value': get_diff(before[key], after[key]),
                }
        else:
            result[key] = {
                'condition': CHANGED,
                'before_value': before[key],
                'after_value': after[key],
                }
    return result
