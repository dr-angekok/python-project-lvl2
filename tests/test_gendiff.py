# -*- coding:utf-8 -*-
"""Users tests."""
import json
from os import popen

import pytest


def simple_out():
    with open('tests/fixtures/json_out.txt', 'r') as file:
        out = file.read()
    return str(out)


def complex_out():
    with open('tests/fixtures/grand_out.txt', 'r') as file:
        out = file.read()
    return str(out)


def plain_out():
    with open('tests/fixtures/plain_out.txt', 'r') as file:
        out = file.read()
    return str(out)


def json_out():
    with open('tests/fixtures/json_format_out.txt', 'r') as file:
        out = file.read()
    return str(out)


@pytest.mark.parametrize("file1,file2,param,expected", [
    ('tests/fixtures/file1.yaml', 'tests/fixtures/file2.yaml', '', simple_out()),
    ('tests/fixtures/grand_file1.yaml', 'tests/fixtures/grand_file2.yaml', '', complex_out()),
    ('tests/fixtures/grand_file1.json', 'tests/fixtures/grand_file2.json', '-f plain', plain_out())
    ])
def test_with_cli(file1, file2, param, expected):
    result = str(popen('poetry run gendiff {0} {1} {2}'.format(file1, file2, param)).read())
    assert result == expected


def test_json_out():
    result = str(popen('poetry run gendiff tests/fixtures/grand_file1.json tests/fixtures/grand_file2.json -f json').read())
    assert json.loads(result) == json.loads(json_out())
