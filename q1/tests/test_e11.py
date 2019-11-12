import os
import time

import pytest

from e11 import (
    timer,
    suppress,
    standard_output,
    temporary_file,
    temporary_directory,
)


def test_timer():
    started = time.time()
    with timer() as timer_:
        time.sleep(1)
    stopped = time.time()
    assert abs(timer_.started - started) < 0.1
    assert abs(timer_.stopped - stopped) < 0.1
    assert 1 <= timer_.elapsed <= 2


def test_timer_error():
    started = time.time()
    with pytest.raises(ValueError):
        with timer() as timer_:
            raise ValueError()
    stopped = time.time()
    assert abs(timer_.started - started) < 0.1
    assert abs(timer_.stopped - stopped) < 0.1
    assert 0 <= timer_.elapsed <= 1


def test_suppress():
    with suppress(NameError, TypeError):
        raise NameError()
    with suppress(NameError, TypeError):
        raise TypeError()


def test_no_suppress():
    with pytest.raises(ValueError):
        with suppress(NameError, TypeError):
            raise ValueError()


def test_suppress_all():
    with suppress():
        raise NameError()
    with suppress():
        raise TypeError()
    with suppress():
        raise ValueError()

def test_capture():
    with standard_output() as stdout:
        print('Hello, world!')
    assert stdout.value == 'Hello, world!\n'


def test_no_output(capsys):
    with standard_output():
        print('Dead men tell no tales')
    out, err = capsys.readouterr()
    assert out == ''
    assert err == ''


def test_temporary_file():
    with temporary_file() as f:
        assert os.path.isfile(f)
    assert not os.path.exists(f)


def test_temporary_directory():
    with temporary_directory() as d:
        assert os.path.isdir(d)
    assert not os.path.exists(d)
