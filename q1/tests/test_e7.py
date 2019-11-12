import time

import pytest


from e7 import Timer


def test_timer():
    started = time.time()
    with Timer() as timer:
        time.sleep(1)
    stopped = time.time()
    assert abs(timer.started - started) < 0.1
    assert abs(timer.stopped - stopped) < 0.1
    assert 1 <= timer.elapsed <= 2


def test_timer_error():
    started = time.time()
    with pytest.raises(ValueError):
        with Timer() as timer:
            raise ValueError()
    stopped = time.time()
    assert abs(timer.started - started) < 0.1
    assert abs(timer.stopped - stopped) < 0.1
    assert 0 <= timer.elapsed <= 1
