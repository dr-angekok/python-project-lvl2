# -*- coding: utf-8 -*-
"""Json out formatter."""
from json import dumps

from gendiff import generate_diff


def translate_state(in_states):
    """Moves the state to the desired line

    Args:
        in_states (dict): Input state

    Returns:
        dict: output state
    """
    STATES_TO_STR = {
        'unchanged': 'not_toched',
        'new': 'new',
        'old': 'old',
        'add': 'added',
        'del': 'removed',
        'child': 'folded',
        }
    translated_state = {}
    for key in STATES_TO_STR:
        translated_state[in_states[key]] = STATES_TO_STR[key]
    return translated_state


def formatting(difference, parent=None):
    """Create a dictionary.

    Args:
        difference: diff from generate_diff module or line
        parent: head befor line

    Returns:
        result(dict): output dict
    """
    states = translate_state(generate_diff.STATES)
    diffs_dict = {}
    for line in difference:
        state = states[generate_diff.get_state(line)]
        key = generate_diff.get_key(line)
        diff_value = generate_diff.get_value(line)
        if parent is None:
            current_key = str(key)
        else:
            current_key = '{0}.{1}'.format(parent, key)
        if generate_diff.is_child(diff_value):
            formated_value = formatting(diff_value, current_key)
            diffs_dict[current_key] = {state: formated_value}
        else:
            diffs_dict[current_key] = {state: diff_value}
    return diffs_dict


def make_json_out(diff):
    """Make json formated output.

    Args:
        diff: diffs frome generate_diff module.

    Returns:
        json_output(str): Json output
    """
    formatted_diff = formatting(diff)
    json_str = dumps(formatted_diff, indent=4, sort_keys=True)
    if not formatted_diff:
        return '{\n}'
    return json_str
