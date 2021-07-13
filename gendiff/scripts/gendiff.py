#!/usr/bin/env python3
"""Diff make programm."""

from gendiff.cli import arg_parser
from gendiff import generate_diff


def main():
    """Diff make programm."""
    first_file, second_file, command = arg_parser()
    print(generate_diff(first_file, second_file, command))


if __name__ == '__main__':
    main()
