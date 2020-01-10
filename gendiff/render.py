# Takes two sets and returns the difference as a string
def string_diff(dictionary, level=1):
    in_after, in_before, indent2, indent4 = ('+ ', '- ', '  ', '    ')
    result = ''
    for key in sorted(dictionary):
        if key:
            result += '\n'
        if dictionary[key]['condition'] == 'in_before':
            if type(dictionary[key]['value']) is dict:
                result += '{}{}{}: {{\n{}{}\n{}}}'.format(indent2 + (indent4 * (level - 1)), in_before, key, indent4 * (level + 1), get_format(dictionary[key]['value']), indent4 * level)
            else:
                result += '{}{}{}: {}'.format(indent2 + (indent4 * (level - 1)), in_before, key, get_string(dictionary[key]['value']))
        if dictionary[key]['condition'] == 'in_after':
            if type(dictionary[key]['value']) is dict:
                result += '{}{}{}: {{\n{}{}\n{}}}'.format(indent2 + (indent4 * (level - 1)), in_after, key, indent4 * (level + 1), get_format(dictionary[key]['value']), indent4 * level)
            else:
                result += '{}{}{}: {}'.format(indent2 + (indent4 * (level - 1)), in_after, key, get_string(dictionary[key]['value']))
        if dictionary[key]['condition'] == 'same':
            if type(dictionary[key]['value']) is dict:
                result += '{}{}{}: {{\n{}{}\n{}}}'.format(indent2, indent2 + (indent4 * (level - 1)), key, indent4 * (level + 1), get_format(dictionary[key]['value']), indent4 * level)
            else:
                result += '{}{}: {}'.format(indent4 * level, key, get_string(dictionary[key]['value']))
        if dictionary[key]['condition'] == 'changed':
            if type(dictionary[key]['before_value']) is dict:
                result += '{}{}{}: {{\n{}{}{}\n{}}}'.format(indent2  + (indent4 * (level - 1)), in_before, key, indent4 * (level + 1), get_format(dictionary[key]['before_value']), indent4 * level)
            if type(dictionary[key]['after_value']) is dict:
                result += '{}{}{}: {{\n{}{}{}\n{}}}'.format(indent2  + (indent4 * (level - 1)), in_after, key, indent4 * (level + 1), get_format(dictionary[key]['after_value']), indent4 * level)            
            else:
                result += '{}{}{}: {}\n'.format(indent2  + (indent4 * (level - 1)), in_before, key, get_string(dictionary[key]['before_value']))
                result += '{}{}{}: {}'.format(indent2  + (indent4 * (level - 1)), in_after, key, get_string(dictionary[key]['after_value']))
        if dictionary[key]['condition'] == 'children':
            result += '{}{}: {{'.format(indent4 * level, key)
            result += string_diff(dictionary[key]['value'], level + 1)
            result += '\n{}}}'.format(indent4 * level)
    if level == 1:
        result = '{' + result + '\n}'
    return result


def get_format(value_is_dict):
    for key, value in value_is_dict.items():
        return '{}: {}'.format(key, value)


def get_string(value_is_not_dict):
    if type(value_is_not_dict) is bool:
        return str(value_is_not_dict).lower()
    else:
        return str(value_is_not_dict)
