from gendiff.constants import IN_BEFORE, IN_AFTER, SAME, CHANGED, CHILDREN


# The function accepts a dictionary
# in which the collected data compares two files
# and returns a string looks like JSON
def string_diff(dictionary, level=0):
    result = ''
    for key in sorted(dictionary):
        indent = '    ' * level

        # Get string format of values
        def get_format(data):
            if type(data) is dict:
                for k, v in data.items():
                    return '{{\n        {}{}: {}\n{}    }}'.format(
                        indent, k, v, indent)
            return data

        if key:
            result += '\n'
        if dictionary[key]['condition'] == IN_BEFORE:
            result += '{}  - {}: {}'.format(
                indent, key, get_format(dictionary[key]['value']))
        if dictionary[key]['condition'] == IN_AFTER:
            result += '{}  + {}: {}'.format(
                indent, key, get_format(dictionary[key]['value']))
        if dictionary[key]['condition'] == SAME:
            result += '{}    {}: {}'.format(
                indent, key, get_format(dictionary[key]['value']))
        if dictionary[key]['condition'] == CHANGED:
            result += '{}  - {}: {}\n'.format(
                indent, key,
                get_format(dictionary[key]['before_value']))
            result += '{}  + {}: {}'.format(
                indent, key,
                get_format(dictionary[key]['after_value']))
        if dictionary[key]['condition'] == CHILDREN:
            result += '    {}{}: {{'.format(indent, key)
            result += string_diff(dictionary[key]['value'], level + 1)
            result += '\n{}    }}'.format(indent)

    if level == 0:
        result = '{' + result + '\n}'
    return result
