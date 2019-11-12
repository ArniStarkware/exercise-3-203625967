import os

from e10a import TemporaryFile
from e10b import TemporaryDirectory


def test_temporary_file():
    with TemporaryFile() as f:
        assert os.path.isfile(f)
    assert not os.path.exists(f)


def test_temporary_directory():
    with TemporaryDirectory() as d:
        assert os.path.isdir(d)
    assert not os.path.exists(d)
