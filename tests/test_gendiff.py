# -*- coding:utf-8 -*-
"""Users tests."""

from gendiff.gendiff import generate_diff

simple_out = ''.join(open('tests/fixtures/json_out.txt', 'r'))

def test_full_load_json():
    assert generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json') == str(simple_out)


def test_full_load_yaml():
    assert generate_diff('tests/fixtures/file1.yaml', 'tests/fixtures/file2.yaml') == str(simple_out)


def test_full_load_yml():
    assert generate_diff('tests/fixtures/file1.yml', 'tests/fixtures/file2.yml') == str(simple_out)

