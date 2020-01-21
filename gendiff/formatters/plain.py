from gendiff.constants import (IN_BEFORE, IN_AFTER, CHANGED, CHILDREN,
                               CONDITION, VALUE, BEFORE_VALUE, AFTER_VALUE)


# A simple format that shows what values ​​have been changed
def output(dictionary, path=None):
    result = []
    for key in sorted(dictionary):
        condition = dictionary[key][CONDITION]
        format_path = get_path(key, path)
        if condition == CHILDREN:
            result.append(output(dictionary[key][VALUE], key))
        elif condition == IN_BEFORE:
            result.append(f"Property '{format_path}' was removed")
        elif condition == IN_AFTER:
            value = get_str_value(dictionary[key][VALUE])
            result.append(
                f"Property '{format_path}' was added with value: '{value}'"
            )
        elif condition == CHANGED:
            before_value = get_str_value(dictionary[key][BEFORE_VALUE])
            after_value = get_str_value(dictionary[key][AFTER_VALUE])
            result.append(
                f"Property '{format_path}' was changed. "
                f"From '{before_value}' to '{after_value}'"
            )
    return '\n'.join(result)


def get_str_value(data):
    if isinstance(data, dict):
        return 'complex value'
    elif type(data) is bool:
        return str(data).lower()
    else:
        return str(data)


def get_path(key_name, path):
    if path is None:
        return key_name
    else:
        return f'{path}.{key_name}'
