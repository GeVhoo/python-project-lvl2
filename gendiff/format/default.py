from gendiff.constants import (IN_BEFORE, IN_AFTER, CHANGED, SAME,
                               CONDITION, VALUE)


# The function accepts a dictionary
# in which the collected data compares two files
# and returns a string looks like JSON
def format(dictionary, level=0):
    result = []
    for key, node in sorted(dictionary.items()):
        indent = '    ' * level
        condition = node[CONDITION]

        # Get string format of values
        def get_format(data):
            if isinstance(data, dict):
                for k, v in data.items():
                    return (f'{{\n        {indent}{k}: '
                            f'{get_str_value(v)}\n{indent}    }}')
            else:
                return get_str_value(data)

        line_template = f'{indent}  {{symbol}} {key}: {{value}}'

        def append(symbol, x):
            result.append(line_template.format(
                symbol=symbol,
                value=get_format(x),
            ))

        value = node[VALUE]

        if condition == IN_BEFORE:
            append('-', value)
        elif condition == IN_AFTER:
            append('+', value)
        elif condition == SAME:
            append(' ', value)
        elif condition == CHANGED:
            old, new = value
            append('-', old)
            append('+', new)
        else:
            result.append(f'    {indent}{key}: {{')
            result.append(format(value, level + 1))
            result.append(f'{indent}    }}')

    if level == 0:
        result = ['{'] + result + ['}']
    return '\n'.join(result)


def get_str_value(item):
    if isinstance(item, bool):
        return str(item).lower()
    else:
        return str(item)
