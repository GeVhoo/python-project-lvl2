from gendiff.formatters import json, plain, string
from gendiff import parsers
from gendiff import generate_diff


def run(first_file, second_file, formatter):
    FORMATTERS = {'json': json, 'plain': plain, 'string': string}
    print(FORMATTERS[formatter].output(generate_diff.get_diff(
        parsers.get_set(first_file),
        parsers.get_set(second_file))))
