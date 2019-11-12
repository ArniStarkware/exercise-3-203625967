import pytest

from e5 import LazyVariable


@pytest.fixture
def x():
    return LazyVariable('x')


@pytest.fixture
def y():
    return LazyVariable('y')


def test_name(x, y):
    assert repr(x) == 'x'
    assert repr(y) == 'y'


def test_pos(x, y):
    assert repr(+x) == '+x'
    assert repr(+y) == '+y'


def test_neg(x, y):
    assert repr(-x) == '-x'
    assert repr(-y) == '-y'


def test_add(x, y):
    assert repr(x + 1) == '(x + 1)'
    assert repr(y + 2) == '(y + 2)'
    assert repr(x + y) == '(x + y)'
    assert repr(y + x) == '(y + x)'


def test_radd(x):
    assert repr(1 + x) == '(1 + x)'


def test_sub(x, y):
    assert repr(x - 1) == '(x - 1)'
    assert repr(y - 2) == '(y - 2)'
    assert repr(x - y) == '(x - y)'
    assert repr(y - x) == '(y - x)'


def test_rsub(x):
    assert repr(1 - x) == '(1 - x)'


def test_mul(x, y):
    assert repr(x * 1) == '(x * 1)'
    assert repr(y * 2) == '(y * 2)'
    assert repr(x * y) == '(x * y)'
    assert repr(y * x) == '(y * x)'


def test_rmul(x):
    assert repr(1 * x) == '(1 * x)'


def test_div(x, y):
    assert repr(x / 1) == '(x / 1)'
    assert repr(y / 2) == '(y / 2)'
    assert repr(x / y) == '(x / y)'
    assert repr(y / x) == '(y / x)'


def test_rdiv(x):
    assert repr(1 / x) == '(1 / x)'


def test_compound(x):
    assert repr(2*x +  1) == '((2 * x) + 1)'


def test_evaluate_1(x):
    assert x.evaluate(x=2) == 2
    assert (x + 1).evaluate(x=2) == 3
    assert (2 * x).evaluate(x=2) == 4
    assert (2 * x + 1).evaluate(x=2) == 5


def test_evaluate_2(x, y):
    assert (x + y).evaluate(x=1, y=2) == 3
    assert (y + x).evaluate(x=1, y=2) == 3
    assert (x / y).evaluate(x=4, y=2) == 2
    assert (y / x).evaluate(x=4, y=2) == 0.5
