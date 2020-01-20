#!/usr/bin/env python3

from gendiff import engine


def main():
    args = engine.parser.parse_args()
    engine.run(args)


if __name__ == '__main__':
    main()
