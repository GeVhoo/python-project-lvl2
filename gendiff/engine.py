from gendiff import format
from gendiff import loader
from gendiff import diff
import argparse


def formatter(name):
    if name == format.JSON:
        return format.json
    elif name == format.PLAIN:
        return format.plain
    elif name == format.DEFAULT:
        return format.default
    raise argparse.ArgumentTypeError(
        f"Unknown formatter: {name}")


parser = argparse.ArgumentParser(description='Generate diff')
parser.add_argument('first_file', type=str, help='input name')
parser.add_argument('second_file', type=str, help='input name')
parser.add_argument('-f', '--format',
                    default=format.DEFAULT,
                    type=formatter,
                    help='set format of output: "string", "plain", "json"')


def run(args):
    print(args.format(diff.get(
        loader.load(args.first_file),
        loader.load(args.second_file),
        )))
