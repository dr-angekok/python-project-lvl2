"""File diff make programm."""

import json
import yaml
from os import path


def get_parse_metod(source):
    """Get parse metod.

    Args:
        path (str): path to the file o other source

    Returns:
        str: extension without period
    """
    return path.splitext(source)[1][1:]


def get_diff(source1, source2):
    """Return diff betwin tow sources.

    Args:
        source1 (dict): source (dict)
        source2 (dict): source (dict)

    Returns:
        str: difference string
    """
    source_diff = [form('-', key, source1[key]) for key in source1.keys() - source2.keys()] # noqa E501
    source_diff += [form('+', key, source2[key]) for key in source2.keys() - source1.keys()] # noqa E501
    for key in source1.keys() & source2.keys():
        if source1[key] == source2[key]:
            source_diff.append(form(' ', key, source1[key]))
        else:
            source_diff.append(form('-', key, source1[key]))
            source_diff.append(form('+', key, source2[key]))

    source_diff.sort(key=lambda string: string[3:5])
    diff_string = '\n'.join(source_diff)

    return '{{\n{0}\n}}'.format(diff_string)


def form(sign, value1, value2):
    """Format a string to a specific format.

    Args:
        sign (str): sign of differec (' ', '+', '-')
        value1 (str): key
        value2 (str): value

    Returns:
        str: formated string
    """
    return '  {0} {1}: {2}'.format(sign, value1, value2)


def generate_diff(file_path1, file_path2):
    """Make difference from tow files.

    Args:
        file_path1 (str): path of 1 file
        file_path2 (str): path of 2 file

    Returns:
        str: formated difference output
    """
    parsers = {
        'json': lambda par: json.load(open(par)),
        'yaml': lambda par: yaml.safe_load(open(par)),
        'yml': lambda par: yaml.safe_load(open(par))
    }
    parsed_data1 = parsers[get_parse_metod(file_path1)](file_path1)
    parsed_data2 = parsers[get_parse_metod(file_path2)](file_path2)
    return get_diff(parsed_data1, parsed_data2)
