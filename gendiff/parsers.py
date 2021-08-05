"""Read sourse module."""

import json

import yaml


def parser(input_data, type_of_data):
    """Parse input_data from a specific format into a dict.

    Args:
        input_data (some format): input data
        type_of_data (str): input data format

    Returns:
        [type]: [description]
    """
    parsers = {
        'json': json.loads,
        'yaml': yaml.safe_load,
        'yml': yaml.safe_load,
    }
    return parsers[type_of_data](input_data)
