"""Choosing an output format."""

from gendiff.formats.json_out import make_json_out
from gendiff.formats.plain import make_plain
from gendiff.formats.stylish import make_stylish


def get_format(form):
    """Return the desired formatting function.

    Args:
        form (str): imput format command

    Raises:
        NotImplementedError: raise if format is wrong type

    Returns:
        function: formating function
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
    return formaters[form]
