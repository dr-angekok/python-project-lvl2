"""Read sourse module."""

import json
from os import path

import yaml


def get_parse_metod(source):
    """Get parse metod.

    Args:
        source (str): path to the file o other source

    Returns:
        str: extension without period
    """
    parsers = {
        'json': lambda par: json.loads(read_file(par)),
        'yaml': lambda par: yaml.safe_load(read_file(par)),
        'yml': lambda par: yaml.safe_load(read_file(par)),
    }

    extension = path.splitext(source)[1][1:]
    return parsers[extension]


def read_file(path):
    """Open file and return loaded text.

    Args:
        path (str): path to the file

    Returns:
        file: readed file
    """
    with open(path, 'r') as f_obj:
        diff = f_obj.read()
    return diff


def parser(path):
    """Return readed source.

    Args:
        path (str): path to sourse

    Returns:
        data: readed data
    """
    return get_parse_metod(path)(path)
