import pytest

from e3 import TransformDict


@pytest.fixture
def td():
    td = TransformDict(lambda key: key.lower())
    td['x'] = 1
    td['y'] = 2
    return td


def test_repr(td):
    assert repr(td) == "{'x': 1, 'y': 2}"


def test_eq(td):
    assert td == td
    td2 = TransformDict(lambda key: key.lower())
    td2['x'] = 1
    td2['y'] = 2
    assert td == td2


def test_ne_1(td):
    td2 = TransformDict(lambda key: key.upper())
    td['x'] = 1
    td['y'] = 2
    assert td != td2


def test_ne_2(td):
    td2 = TransformDict(lambda key: key.lower())
    td['x'] = 1
    assert td != td2
    td['y'] = 2
    td['z'] = 3
    assert td != td2


def test_ne_3(td):
    assert td != 1
    assert td != 'Hello, world!'


def test_bool(td):
    assert bool(td) is True
    td2 = TransformDict(lambda key: key.lower())
    assert bool(td2) is False


def test_getitem(td):
    assert td['x'] == 1
    assert td['X'] == 1
    assert td['y'] == 2
    assert td['Y'] == 2


def test_getitem_error(td):
    with pytest.raises(KeyError):
        td['z']


def test_setitem(td):
    td['z'] = 3
    assert td['Z'] == 3
    td['Z'] = 4
    assert td['z'] == 4


def test_delitem(td):
    del td['x']
    with pytest.raises(KeyError):
        td['x']


def test_delitem_error(td):
    del td['x']
    with pytest.raises(KeyError):
        del td['x']
    with pytest.raises(KeyError):
        del td['z']


def test_len(td):
    assert len(td) == 2
    td['X'] = 0
    assert len(td) == 2
    td['Y'] = 0
    assert len(td) == 2
    td['Z'] = 0
    assert len(td) == 3


def test_contains(td):
    assert 'x' in td
    assert 'X' in td
    assert 'y' in td
    assert 'Y' in td
    assert 'z' not in td
    assert 'Z' not in td


def test_iter(td):
    assert list(td) == ['x', 'y']
