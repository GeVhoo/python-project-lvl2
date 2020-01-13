from gendiff.constants import IN_BEFORE, IN_AFTER, SAME


def string_diff(dictionary, level=0):
    result = ''
    for key in sorted(dictionary):
        indent = '    ' * level

        def get_format(data):
            if type(data) is dict:
                for k, v in data.items():
                    return '{{\n        {}{}: {}\n{}    }}'.format(
                        indent, k, v, indent)
            if type(data) is bool:
                return str(data).lower()
            else:
                return str(data)

        if key:
            result += '\n'
        if dictionary[key]['condition'] == IN_BEFORE:
            result += '{}{}{}: {}'.format(
                indent, IN_BEFORE, key, get_format(dictionary[key]['value']))
        if dictionary[key]['condition'] == IN_AFTER:
            result += '{}{}{}: {}'.format(
                indent, IN_AFTER, key, get_format(dictionary[key]['value']))
        if dictionary[key]['condition'] == SAME:
            result += '{}{}{}: {}'.format(
                indent, SAME, key, get_format(dictionary[key]['value']))
        if dictionary[key]['condition'] == 'changed':
            result += '{}{}{}: {}\n'.format(
                indent, IN_BEFORE, key,
                get_format(dictionary[key]['before_value']))
            result += '{}{}{}: {}'.format(
                indent, IN_AFTER, key,
                get_format(dictionary[key]['after_value']))
        if dictionary[key]['condition'] == 'children':
            result += '    {}{}: {{'.format(indent, key)
            result += string_diff(dictionary[key]['value'], level + 1)
            result += '\n{}    }}'.format(indent)

    if level == 0:
        result = '{' + result + '\n}'
    return result