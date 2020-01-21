from gendiff.constants import (IN_BEFORE, IN_AFTER, CHANGED, SAME,
                               CONDITION, VALUE, BEFORE_VALUE, AFTER_VALUE)


# The function accepts a dictionary
# in which the collected data compares two files
# and returns a string looks like JSON
def output(dictionary, level=0):
    result = []
    for key in sorted(dictionary):
        indent = '    ' * level
        condition = dictionary[key][CONDITION]

        # Get string format of values
        def get_format(data):
            if isinstance(data, dict):
                for k, v in data.items():
                    return (f'{{\n        {indent}{k}: '
                            f'{get_str_value(v)}\n{indent}    }}')
            else:
                return get_str_value(data)

        if condition == IN_BEFORE:
            value = get_format(dictionary[key][VALUE])
            result.append(f'{indent}  - {key}: {value}')
        elif condition == IN_AFTER:
            value = get_format(dictionary[key][VALUE])
            result.append(f'{indent}  + {key}: {value}')
        elif condition == SAME:
            value = get_format(dictionary[key][VALUE])
            result.append(f'{indent}    {key}: {value}')
        elif condition == CHANGED:
            before_value = get_format(dictionary[key][BEFORE_VALUE])
            after_value = get_format(dictionary[key][AFTER_VALUE])
            result.append(f'{indent}  - {key}: {before_value}')
            result.append(f'{indent}  + {key}: {after_value}')
        else:
            result.append(f'    {indent}{key}: {{')
            result.append(output(dictionary[key][VALUE], level + 1))
            result.append(f'{indent}    }}')

    if level == 0:
        result = ['{'] + result + ['}']
    return '\n'.join(result)


def get_str_value(item):
    if isinstance(item, bool):
        return str(item).lower()
    else:
        return str(item)
