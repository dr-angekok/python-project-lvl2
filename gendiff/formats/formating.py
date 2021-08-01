"""Choosing an output format."""

from gendiff.formats.json_out import make_json_out
from gendiff.formats.plain import make_plain
from gendiff.formats.stylish import make_stylish


def make_formatted(form, diff):
    """Return the formatted output.

    Args:
        form (str): imput format command
        diff (diff): input diff

    Raises:
        NotImplementedError: raise if format is wrong type

    Returns:
        str: formatted output
    """
    if form is None:
        form = 'stylish'
    formaters = {
        'stylish': make_stylish,
        'plain': make_plain,
        'json': make_json_out,
    }
    if form not in formaters.keys():
        raise NotImplementedError('"{0}" is wrong out format type!'.format(form))
    return formaters[form](diff)
