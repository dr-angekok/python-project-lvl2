# -*- coding:utf-8 -*-
"""Users tests."""
from os import popen


simple_out = ''.join(open('tests/fixtures/json_out.txt', 'r'))
complex_out = ''.join(open('tests/fixtures/grand_out.txt', 'r'))
plain_out = ''.join(open('tests/fixtures/plain_out.txt', 'r'))


def test_gendiff_cli_flat():
    result = popen('poetry run gendiff tests/fixtures/file1.yaml tests/fixtures/file2.yaml').read()
    assert str(result) == str(simple_out)


def test_grandiff_cli_flat():
    result = popen('poetry run gendiff tests/fixtures/grand_file1.yaml tests/fixtures/grand_file2.yaml').read()
    assert str(result) == str(complex_out)


def test_grandiff_cli_plain():
    result = popen('poetry run gendiff tests/fixtures/grand_file1.json tests/fixtures/grand_file2.json -f plain').read()
    assert str(result) == str(plain_out)