import pytest

from e4 import MultiDict


@pytest.fixture
def md():
    md = MultiDict()
    md['x'] = 1
    md['x'] = 2
    md['y'] = 2
    return md


def test_repr(md):
    assert repr(md) == "{'x': [1, 2], 'y': [2]}"


def test_eq(md):
    assert md == md
    md2 = MultiDict()
    md2['x'] = 1
    md2['x'] = 2
    md2['y'] = 2
    assert md == md2


def test_ne_1(md):
    md2 = MultiDict()
    md['x'] = 1
    md['y'] = 2
    assert md != md2


def test_ne_2(md):
    md2 = MultiDict()
    md['x'] = 1
    md['x'] = 2
    assert md != md2
    md['y'] = 2
    md['y'] = 3
    assert md != md2


def test_ne_3(md):
    assert md != 1
    assert md != 'Hello, world!'


def test_bool(md):
    assert bool(md) is True
    md2 = MultiDict()
    assert bool(md2) is False


def test_getitem(md):
    assert md['x'] == 1
    assert md['y'] == 2


def test_getitem_error(md):
    with pytest.raises(KeyError):
        md['z']


def test_setitem(md):
    md['z'] = 3
    assert md['z'] == 3
    md['z'] = 4
    assert md['z'] == 3


def test_setitem_order(md):
    md['z'] = 1
    md['z'] = 2
    assert md['z'] == 1
    del md['z']
    assert md['z'] == 2


def test_delitem(md):
    del md['x']
    del md['x']
    with pytest.raises(KeyError):
        md['x']
    del md['y']
    with pytest.raises(KeyError):
        md['y']


def test_delitem_error(md):
    del md['x']
    del md['x']
    with pytest.raises(KeyError):
        del md['x']
    del md['y']
    with pytest.raises(KeyError):
        del md['y']
    with pytest.raises(KeyError):
        del md['z']


def test_len(md):
    assert len(md) == 2
    md['x'] = 0
    assert len(md) == 2
    md['y'] = 0
    assert len(md) == 2
    md['z'] = 0
    assert len(md) == 3


def test_contains(md):
    assert 'x' in md
    assert 'y' in md
    assert 'z' not in md


def test_iter(md):
    assert list(md) == ['x', 'y']


def test_get_all(md):
    assert md.get_all('x') == [1, 2]
    assert md.get_all('y') == [2]


def test_delete_all(md):
    md.delete_all('x')
    with pytest.raises(KeyError):
        md['x']
