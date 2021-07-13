# -*- coding: utf-8 -*-
"""Plain formater fo diffs"""

from gendiff import generate_diff


def make_plain(diff):
    """Generate a plain format.

    Args:
        diff: difference

    Returns:
        str: formated diff in a string.
    """
    plaint_output = generate_plain_string(diff)
    if plaint_output:
        return plaint_output[:-1]
    return '{\n}'


def generate_plain_string(diffs, forward_line=''):
    """Generate a plain string format.

    Args:
        diffs: some diffs
        forward_line: the line string befo call

    Returns:
        str: formated output string.
    """
    output_string = ''
    for line in diffs:
        state = generate_diff.get_state(line)
        key = generate_diff.get_key(line)
        diff_value = generate_diff.get_value(line)
        if forward_line:
            head_str = '{0}.{1}'.format(forward_line, key)
        else:
            head_str = key

        key_str = "Property '{0}' was".format(head_str)

        if isinstance(diff_value, bool):
            val_str = 'true' if diff_value else 'false'
        elif diff_value is None:
            val_str = 'null'
        elif isinstance(diff_value, str):
            val_str = "'{0}'".format(diff_value)
        elif isinstance(diff_value, (int, float, complex)):
            val_str = str(diff_value)
        else:
            val_str = '[complex value]'

        if state == generate_diff.STATES['child']:
            output_string += generate_plain_string(diff_value, head_str)
        elif state == generate_diff.STATES['old']:
            output_string += '{0} updated. From {1} to '.format(key_str, val_str)
        elif state == generate_diff.STATES['new']:
            output_string += '{0}\n'.format(val_str)
        elif state == generate_diff.STATES['add']:
            output_string += '{0} added with value: {1}\n'.format(key_str, val_str)
        elif state == generate_diff.STATES['del']:
            output_string += '{0} removed\n'.format(key_str)
    return output_string
