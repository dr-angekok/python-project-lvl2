# -*- coding:utf-8 -*-
"""Users tests."""
import json

import pytest
from gendiff import generate_diff


def make_path(file):
    PATH = 'tests/fixtures/'
    return '{0}{1}'.format(PATH, file)


def read_out_exs(filename):
    with open(make_path(filename), 'r') as file:
        out = file.read()
    return str(out)


@pytest.mark.parametrize("file1,file2,param,exs", [
    ('file1.yaml', 'file2.yaml', 'stylish', 'json_out.txt'),
    ('grand_file1.yaml', 'grand_file2.yaml', 'stylish', 'grand_out.txt'),
    ('grand_file1.json', 'grand_file2.json', 'plain', 'plain_out.txt')])
def test_generate_diff(file1, file2, param, exs):
    expected = read_out_exs(exs)
    result = generate_diff(make_path(file1), make_path(file2), param)
    assert result == expected


def test_json_out():
    result = generate_diff(make_path('grand_file1.json'), make_path('grand_file2.json'), 'json')
    assert json.loads(result) == json.loads(read_out_exs('json_format_out.txt'))
