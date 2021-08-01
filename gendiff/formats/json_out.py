# -*- coding: utf-8 -*-
"""Json out formatter."""

from json import dumps

from gendiff.states import STATES, STATES_TO_JSON


def translate_state(in_states):
    """Move the state to the desired line.

    Args:
        in_states (dict): Input state

    Returns:
        dict: output state
    """
    translated_state = {}
    for key in STATES_TO_JSON:
        translated_state[in_states[key]] = STATES_TO_JSON[key]
    return translated_state


def formatting(difference, parent=None):
    """Create a dictionary.

    Args:
        difference: diff from gendiff module or line
        parent: head befor line

    Returns:
        result(dict): output dict
    """
    states = translate_state(STATES)
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
