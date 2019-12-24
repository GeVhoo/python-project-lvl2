# Takes two sets and returns the difference as a string
def generate_diff(first_file, second_file):
    # Get the difference in the files
    without_changes = (first_file & second_file)
    in_first_file = (first_file - second_file)
    in_second_file = (second_file - first_file)
    # Collect a list of differences with the symbol
    diff_list = []
    add, sub, non = ('+ ', '- ', '  ')
    for item in without_changes:
        diff_list += [(non, item[0], item[1])]
    for item in in_first_file:
        diff_list += [(sub, item[0], item[1])]
    for item in in_second_file:
        diff_list += [(add, item[0], item[1])]
    # Format and return the string
    formating = '  {}{}: {}'

    def key(x):
        return x[1]

    diff_list.sort(key=key)
    result = ''
    for i in diff_list:
        if i:
            result += '\n'
        result += formating.format(i[0], i[1], i[2])
    return ('{' + result + '\n}')
