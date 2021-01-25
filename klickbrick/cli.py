import argparse
import sys


def main(args=None):
    if not args:
        args = sys.argv[1:]

    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    hello = subparsers.add_parser("hello", help="prints hello")
    hello.add_argument("--name", type=str)

    parsed_args = parser.parse_args(args)

    if parsed_args.name:
        output = f"Hello {parsed_args.name}"
    else:
        output = "Hello World"

    print(output)
    return output


if __name__ == "__main__":
    main(sys.argv[1:])
