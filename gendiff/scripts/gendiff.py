#!/usr/bin/env python3
"""Diff make programm."""

from gendiff import generate_diff
from gendiff.cli import parse_args


def main():
    """Diff make programm."""
    first_file, second_file, command = parse_args()
    print(generate_diff(first_file, second_file, command))


if __name__ == '__main__':
    main()
