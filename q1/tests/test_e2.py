import inspect

import pytest

from e2 import walk


@pytest.fixture
def fs(tmp_path):
    d1 = tmp_path / 'd1'
    d1.mkdir()
    f1 = tmp_path / 'f1'
    f1.write_text('1')
    d2 = d1 / 'd2'
    d2.mkdir()
    f2 = d1 / 'f2'
    f2.write_text('2')
    d3 = d2 / 'd3'
    d3.mkdir()
    d4 = d2 / 'd4'
    d4.mkdir()
    f3 = d3 / 'f3'
    f3.write_text('3')
    return tmp_path


def test_walk(fs):
    expected = [
        ('d1', 'directory'),
        ('f1', 'file'),
        ('d2', 'directory'),
        ('f2', 'file'),
        ('d3', 'directory'),
        ('d4', 'directory'),
        ('f3', 'file'),
    ]
    for entry, (name, type) in zip(walk(fs), expected):
        assert entry.name == name
        assert entry.type == type


def test_skip(fs):
    entries = []
    for entry in walk(fs):
        entries.append(entry.name)
        if entry.name == 'd2':
            entry.skip()
    assert entries == ['d1', 'f1', 'd2', 'f2']


def test_generator():
    assert inspect.isgenerator(walk(None))
