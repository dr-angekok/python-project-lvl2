# -*- coding:utf-8 -*-

"""Users tests."""

from gendiff.gendiff import generate_diff

test_flat_json = ''.join(open('tests/fixtures/json_out.txt', 'r'))

def test_full_load():
    assert generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json') == str(test_flat_json)
