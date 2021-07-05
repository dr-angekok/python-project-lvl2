#!/usr/bin/env python3
"""Diff make programm."""

from gendiff.cli import arg_parser
from gendiff.gendiff import generate_diff


def main():
    """Diff make programm."""
    first_file, second_file, _ = arg_parser()
    print(generate_diff(first_file, second_file))


if __name__ == '__main__':
    main()
