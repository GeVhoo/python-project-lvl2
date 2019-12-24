#!/usr/bin/env python3

import argparse
from gendiff import output
from gendiff.open_file import open_json


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', type=str, help='input name')
    parser.add_argument('second_file', type=str, help='input name')
    parser.add_argument('-f', '--format', type=str, help='set format of output')  # noqa: 501
    args = parser.parse_args()
    first_path = args.first_file
    second_path = args.second_file

    print(output.generate_diff(open_json.get_set(first_path), open_json.get_set(second_path)))  # noqa: 501


if __name__ == '__main__':
    main()
