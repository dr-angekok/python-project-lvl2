"""File diff make programm."""

import json


def load_file(filename):
    """Load file.

    Args:
        filename (str): path to load file

    Returns:
        dict:
    """
    return json.load(open(filename))


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
            source_diff.append(form('+', key, source2[key]))
            source_diff.append(form('-', key, source1[key]))

    source_diff.sort(key=sort_by_alphabet)
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
    return ' {0} {1}: {2}'.format(sign, value1, value2)


def sort_by_alphabet(input_str):
    """Alphabetical sort of input_str by 4 sign.

    Args:
        input_str (str): import string

    Returns:
        str: 4 sing
    """
    return input_str[3:5]


def generate_diff(file_path1, file_path2):
    """Make difference from tow files.

    Args:
        file_path1 (str): path of 1 file
        file_path2 (str): path of 2 file

    Returns:
        str: formated difference output
    """
    file1 = load_file(file_path1)
    file2 = load_file(file_path2)
    return get_diff(file1, file2)
