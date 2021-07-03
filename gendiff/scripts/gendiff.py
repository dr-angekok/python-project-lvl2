#!/usr/bin/env python3
"""Diff make programm."""
import argparse

from gendiff.gendiff import generate_diff


def main():
    """Diff make programm."""
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', metavar='file1.json', type=str)
    parser.add_argument('second_file', metavar='file2.json', type=str)
    parser.add_argument('-f', '--format', help='\n set format of output')
    arguments = parser.parse_args()
    print(generate_diff(arguments.first_file, arguments.second_file))


if __name__ == '__main__':
    main()
