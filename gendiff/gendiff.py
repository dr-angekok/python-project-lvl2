"""File diff make programm."""

from os import path

from gendiff.flags import INTERNAL_STRUCTURE_FLAGS as FLAGS
from gendiff.formats.formating import make_formatted
from gendiff.parsers import parser


def extension_check(extension, extensions):
    """Raise an error if there is no extension in the list of extensions.

    Args:
        extension (str): [description]
        extensions (str): [description]

    Raises:
        NotImplementedError: Raises if the extension is not in list.
    """
    if extension not in extensions:
        raise NotImplementedError('"{0}" is wrong input format type!'.format(extension))


def read_file(path):
    """Open file and return loaded data.

    Args:
        path (str): path to the file

    Returns:
        file: readed file
    """
    with open(path, 'r') as f_obj:
        readed_file = f_obj.read()
    return readed_file


def get_diff(source1, source2):
    """Return diff betwin tow sources.

    Args:
        source1 (dict): source (dict)
        source2 (dict): source (dict)

    Returns:
        difference
    """
    difference = []
    all_keys = sorted(source1.keys() | source2.keys())

    for key in all_keys:
        value1 = source1.get(key)
        value2 = source2.get(key)

        if value1 == value2:
            difference.append((FLAGS['unchanged'], key, value1))
        elif key not in source1:
            difference.append((FLAGS['add'], key, value2))
        elif key not in source2:
            difference.append((FLAGS['del'], key, value1))
        elif isinstance(value1, dict) and isinstance(value2, dict):
            difference.append((FLAGS['child'], key, get_diff(value1, value2)))
        else:
            difference.append((FLAGS['old'], key, value1))
            difference.append((FLAGS['new'], key, value2))
    return difference


def generate_diff(path1, path2, form):
    """Make difference from tow files.

    Args:
        path1 (str): path to source1
        path2 (str): path to source2

    Returns:
        str: formated difference output
    """
    readers = {
        'json': read_file,
        'yaml': read_file,
        'yml': read_file,
    }
    extension1 = path.splitext(path1)[1][1:]
    extension2 = path.splitext(path2)[1][1:]

    extension_check(extension1, readers.keys())
    extension_check(extension2, readers.keys())

    data1 = readers[extension1](path1)
    data2 = readers[extension2](path2)

    return make_formatted(form, get_diff(parser(data1, extension1), parser(data2, extension2)))
