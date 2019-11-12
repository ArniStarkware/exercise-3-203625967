import inspect

import pytest

import e1a
import e1b


@pytest.fixture
def tree():
    return (1, [
        (2, [
            (4, []),
            (5, []),
        ]),
        (3, [
            (6, []),
            (7, []),
        ]),
    ])


def test_e1a_bfs(tree):
    assert list(e1a.bfs(tree)) == [1, 2, 3, 4, 5, 6, 7]


def test_e1a_generator():
    _test_generator(e1a.bfs)


def test_e1b_dfs(tree):
    assert list(e1b.dfs(tree)) == [1, 2, 4, 5, 3, 6, 7]


def test_e1b_generator():
    _test_generator(e1b.dfs)


def _test_generator(g):
    assert inspect.isgenerator(g(None))
