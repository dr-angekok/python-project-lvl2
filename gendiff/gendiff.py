"""File diff make programm."""

from gendiff.formats.formating import make_formatted
from gendiff.states import STATES
from gendiff.parsers import parser


def get_diff(source1, source2):
    """Return diff betwin tow sources.

    Args:
        source1 (dict): source (dict)
        source2 (dict): source (dict)

    Returns:
        difference
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


def generate_diff(path1, path2, form='stylish'):
    """Make difference from tow files.

    Args:
        path1 (str): path to source1
        path2 (str): path to source2

    Returns:
        str: formated difference output
    """
    return make_formatted(form, get_diff(parser(path1), parser(path2)))
