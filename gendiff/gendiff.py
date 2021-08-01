"""File diff make programm."""

import json
from os import path

import yaml

from gendiff.formats.formating import get_format
from gendiff.states import STATES


def get_parse_metod(source):
    """Get parse metod.

    Args:
        source (str): path to the file o other source

    Returns:
        str: extension without period
    """
    return path.splitext(source)[1][1:]


def read_file(path):
    """Open file and return loaded text."""
    with open(path, 'r') as f_obj:
        diff = f_obj.read()
    return diff


def get_diff(source1, source2):
    """Return diff betwin tow sources.

    Args:
        source1 (dict): source (dict)
        source2 (dict): source (dict)

    Returns:
        str: difference dict {(diff, key): value}
    """
    difference = []
    all_keys = sorted(source1.keys() | source2.keys())

    for key in all_keys:
        value1 = source1.get(key)
        value2 = source2.get(key)

        if value1 == value2:
            difference.append((STATES['unchanged'], key, value1))
        elif key not in source1:
            difference.append((STATES['add'], key, value2))
        elif key not in source2:
            difference.append((STATES['del'], key, value1))
        elif isinstance(value1, dict) and isinstance(value2, dict):
            difference.append((STATES['child'], key, get_diff(value1, value2)))
        else:
            difference.append((STATES['old'], key, value1))
            difference.append((STATES['new'], key, value2))
    return difference


def generate_diff(file_path1, file_path2, form='stylish'):
    """Make difference from tow files.

    Args:
        file_path1 (str): path of 1 file
        file_path2 (str): path of 2 file

    Returns:
        str: formated difference output
    """
    parsers = {
        'json': lambda par: json.loads(read_file(par)),
        'yaml': lambda par: yaml.safe_load(read_file(par)),
        'yml': lambda par: yaml.safe_load(read_file(par)),
    }
    parsed_data1 = parsers[get_parse_metod(file_path1)](file_path1)
    parsed_data2 = parsers[get_parse_metod(file_path2)](file_path2)

    return get_format(form)(get_diff(parsed_data1, parsed_data2))
