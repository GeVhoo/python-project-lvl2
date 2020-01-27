from gendiff.constants import (IN_BEFORE, IN_AFTER, CHANGED, CHILDREN,
                               CONDITION, VALUE)


# A simple format that shows what values ​​have been changed
def format(dictionary, path=None):
    result = []
    for key, node in sorted(dictionary.items()):
        condition = node[CONDITION]
        format_path = get_path(key, path)
        value = node[VALUE]
        if condition == CHILDREN:
            result.append(format(value, key))
        elif condition == IN_BEFORE:
            result.append(f"Property '{format_path}' was removed")
        elif condition == IN_AFTER:
            value = get_str_value(value)
            result.append(
                f"Property '{format_path}' was added with value: '{value}'"
            )
        elif condition == CHANGED:
            old, new = value
            before_value = get_str_value(old)
            after_value = get_str_value(new)
            result.append(
                f"Property '{format_path}' was changed. "
                f"From '{before_value}' to '{after_value}'"
            )
    return '\n'.join(result)


def get_str_value(data):
    if isinstance(data, dict):
        return 'complex value'
    elif isinstance(data, bool):
        return str(data).lower()
    else:
        return str(data)


def get_path(key_name, path):
    if path is None:
        return key_name
    else:
        return f'{path}.{key_name}'
