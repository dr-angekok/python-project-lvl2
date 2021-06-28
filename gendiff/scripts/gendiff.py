#!/usr/bin/env python
"""Diff make programm."""
import argparse


def main():
    """Diff make programm."""
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('passes', metavar='first_file', type=str)
    parser.add_argument('passes', metavar='second_file', type=str)
    parser.add_argument('-f', '--format', help='\n set format of output')


if __name__ == '__main__':
    main()
