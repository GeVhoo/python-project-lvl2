from gendiff.formatters import json, plain, string
from gendiff import parsers
from gendiff import generate_diff
import argparse


def formatter(inpute_formate):
    if inpute_formate == 'json':
        return json.output
    elif inpute_formate == 'plain':
        return plain.output
    elif inpute_formate == 'string':
        return string.output


parser = argparse.ArgumentParser(description='Generate diff')
parser.add_argument('first_file', type=str, help='input name')
parser.add_argument('second_file', type=str, help='input name')
parser.add_argument('-f', '--format',
                    default='string',
                    choices=['string', 'plain', 'json'],
                    help='set format of output: "string", "plain", "json"')


def run(args):
    print(formatter(args.format)(generate_diff.get_diff(
        parsers.get_set(args.first_file),
        parsers.get_set(args.second_file))))
