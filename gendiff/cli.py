#!/usr/bin/env python3
"""Cli for the diff make."""
import argparse


def arg_parser():
    """Pars command line parameters.

    Returns:
        tuple: str of first_file, second_file, format
    """
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', metavar='file1.json', type=str)
    parser.add_argument('second_file', metavar='file2.json', type=str)
    parser.add_argument('-f', '--format', help='\n set format of output')
    arguments = parser.parse_args()
    return arguments.first_file, arguments.second_file, arguments.format
