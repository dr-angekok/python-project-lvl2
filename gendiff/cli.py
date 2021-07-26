#!/usr/bin/env python3
"""Cli for the diff make."""
import argparse

FORMAT_HELP_STRING = """
set format of output
stylish -default"""


def parse_args():
    """Pars command line parameters.

    Returns:
        tuple: str of first_file, second_file, format
    """
    parser = argparse.ArgumentParser(description='Generate diff of two files')
    parser.add_argument('first_file', metavar='file1.[json/yaml]', type=str)
    parser.add_argument('second_file', metavar='file2.[json/yaml]', type=str)
    parser.add_argument(
        '-f', '--format',
        default='stylish',
        help=FORMAT_HELP_STRING)
    arguments = parser.parse_args()
    return arguments.first_file, arguments.second_file, arguments.format
