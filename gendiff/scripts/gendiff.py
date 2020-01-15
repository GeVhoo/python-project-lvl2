#!/usr/bin/env python3

import argparse
from gendiff import engine


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', type=str, help='input name')
    parser.add_argument('second_file', type=str, help='input name')
    parser.add_argument('-f', '--format',
                        default='string',
                        help='set format of output: "string", "plain", "json"')
    args = parser.parse_args()
    engine.run(args.first_file, args.second_file, args.format)


if __name__ == '__main__':
    main()
