from gendiff.constants import IN_BEFORE, IN_AFTER


def plain_diff(dictionary, path=[]):
    result = []
    for key in sorted(dictionary):
        path.append(key)
        format_path = '.'.join(path)
        if dictionary[key]['condition'] == 'children':
            result.append(plain_diff(dictionary[key]['value'], path))
        if dictionary[key]['condition'] == IN_BEFORE:
            result.append("Property '{}' was removed".format(format_path))
        if dictionary[key]['condition'] == IN_AFTER:
            description = "Property '{}' was added with value: '{}'"
            result.append(description.format(
                format_path,
                format_value(dictionary[key]['value'])))
        if dictionary[key]['condition'] == 'changed':
            description = "Property '{}' was changed. From '{}' to '{}'"
            result.append(description.format(
                format_path,
                format_value(dictionary[key]['before_value']),
                format_value(dictionary[key]['after_value'])))
        path.pop()
    return '\n'.join(result)


def format_value(data):
    if type(data) is dict:
        return 'complex value'
    if type(data) is bool:
        return str(data).lower()
    else:
        return str(data)
