# -*- coding:utf-8 -*-

"""Users tests."""

from gendiff.gendiff import generate_diff

test_flat_json = ''.join(open('tests/gendiff.txt', 'r'))

def test_full_load():
    assert generate_diff('file1.json', 'file2.json') == str(test_flat_json)
