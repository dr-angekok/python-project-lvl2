# -*- coding: utf-8 -*-
"""Plain formater fo diffs"""

from gendiff.flags import INTERNAL_STRUCTURE_FLAGS as FLAGS


def translate_diff_value(diff_value):
    """Translate values to human language

    Args:
        diff_value (str): some key value

    Returns:
        str: translated value
    """
    if isinstance(diff_value, bool):
        return 'true' if diff_value else 'false'
    elif diff_value is None:
        return 'null'
    elif isinstance(diff_value, str):
        return "'{0}'".format(diff_value)
    elif isinstance(diff_value, (int, float, complex)):
        return str(diff_value)
    return '[complex value]'


def make_plain(diff):
    """Generate a plain format.

    Args:
        diff: difference

    Returns:
        str: formated diff in a string.
    """
    plaint_output = generate_plain_string(diff)
    if plaint_output:
        return plaint_output
    return '{\n}'


def generate_plain_string(diffs, forward_line=''):
    """Generate a plain string format.

    Args:
        diffs: some diffs
        forward_line: the line string befo call

    Returns:
        str: formated output string.
    """
    output_string = []
    iter_lines = iter(diffs)
    for line in iter_lines:
        state = line[0]
        key = line[1]
        diff_value = line[2]
        if forward_line:
            head_str = '{0}.{1}'.format(forward_line, key)
        else:
            head_str = key

        key_str = "Property '{0}' was".format(head_str)
        val_str = translate_diff_value(diff_value)

        if state == FLAGS['child']:
            output_string.append(generate_plain_string(diff_value, head_str))
        elif state == FLAGS['old']:
            next_value_str = translate_diff_value(next(iter_lines)[2])
            output_string.append('{0} updated. From {1} to {2}'.format(key_str, val_str, next_value_str))
        elif state == FLAGS['add']:
            output_string.append('{0} added with value: {1}'.format(key_str, val_str))
        elif state == FLAGS['del']:
            output_string.append('{0} removed'.format(key_str))
    return '\n'.join(output_string)
