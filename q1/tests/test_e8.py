import time

import pytest


from e8 import Suppress


def test_suppress():
    with Suppress(NameError, TypeError):
        raise NameError()
    with Suppress(NameError, TypeError):
        raise TypeError()


def test_no_suppress():
    with pytest.raises(ValueError):
        with Suppress(NameError, TypeError):
            raise ValueError()


def test_suppress_all():
    with Suppress():
        raise NameError()
    with Suppress():
        raise TypeError()
    with Suppress():
        raise ValueError()
