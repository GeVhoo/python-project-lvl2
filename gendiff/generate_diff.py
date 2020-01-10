def get_diff(before, after):
    result = {}
    for key in before:
        if key not in after:
            result[key] = {
                'condition': 'in_before',
                'value': before[key],
                }
    for key in after:
        if key not in before:
            result[key] = {
                'condition': 'in_after',
                'value': after[key],
                }
    for key in before:
        if key in after:
            if before[key] == after[key]:
                result[key] = {
                    'condition': 'same',
                    'value': before[key],
                    }
            elif type(before[key]) is dict and type(after[key]) is dict:
                result[key] = {
                    'condition': 'children',
                    'value': get_diff(before[key], after[key]),
                    }
            else:
                result[key] = {
                    'condition': 'changed',
                    'before_value': before[key],
                    'after_value': after[key],
                    }
    return result
