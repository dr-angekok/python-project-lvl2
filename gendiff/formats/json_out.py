# -*- coding: utf-8 -*-
"""Json out formatter."""

from json import dumps

from gendiff.flags import INTERNAL_STRUCTURE_FLAGS, JSON_FLAGS


def translate_state(in_flags):
    """Move the flags to the desired line.

    Args:
        in_flags (dict): Input state

    Returns:
        dict: output state
    """
    translated_state = {}
    for key in JSON_FLAGS:
        translated_state[in_flags[key]] = JSON_FLAGS[key]
    return translated_state


def formatting(difference, parent=None):
    """Create a dictionary.

    Args:
        difference: diff from gendiff module or line
        parent: head befor line

    Returns:
        result(dict): output dict
    """
    states = translate_state(INTERNAL_STRUCTURE_FLAGS)
    diffs_dict = {}
    for line in difference:
        state = states[line[0]]
        key = line[1]
        diff_value = line[2]
        if parent is None:
            current_key = str(key)
        else:
            current_key = '{0}.{1}'.format(parent, key)
        if isinstance(diff_value, list):
            formated_value = formatting(diff_value, current_key)
            diffs_dict[current_key] = {state: formated_value}
        else:
            diffs_dict[current_key] = {state: diff_value}
    return diffs_dict


def make_json_out(diff):
    """Make json formated output.

    Args:
        diff: diffs frome gendiff module.

    Returns:
        json_output(str): Json output
    """
    formatted_diff = formatting(diff)
    json_str = dumps(formatted_diff, indent=4, sort_keys=True)
    if not formatted_diff:
        return '{\n}'
    return json_str
