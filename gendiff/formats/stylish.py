"""Output formated string."""

IDENT = '    '


def make_stilish_node(diff_val, paragraph):
    """Make a formatted string.

    Args:
        diff_val: list
        paragraph: Levels of recursive call

    Returns:
        str: formatted string
    """
    if isinstance(diff_val, dict):
        string = '{\n'
        for key, key_value in diff_val.items():
            string += '{0}{1}{2}: {3}\n'.format(
                IDENT,
                paragraph,
                key,
                make_stilish_node(key_value, paragraph + IDENT),
            )
        string += '{0}}}'.format(paragraph)
        return string
    if isinstance(diff_val, bool):
        return 'true' if diff_val else 'false'
    if diff_val is None:
        return 'null'
    return str(diff_val)


def make_stylish(difference, level=0):
    """Format item in to string for output.

    Args:
        difference: list in list (state, key, value)
        level: Levels of recursive call

    Returns:
        str: Plain format.
    """
    output_str = '{\n'
    paragraph = IDENT * level

    for line in difference:
        state, key, diff_value = line
        if isinstance(diff_value, list):
            next_string = make_stylish(diff_value, level + 1)
        else:
            next_string = make_stilish_node(diff_value, paragraph + IDENT)
        output_str += '{0}  {1} {2}: {3}\n'.format(
            paragraph,
            state,
            key,
            next_string,
            )
    output_str += '{0}}}'.format(paragraph)
    return output_str
