import os

import pytest


@pytest.fixture(autouse=True)
def d(tmp_path):
    d1 = tmp_path / 'd1'
    d1.mkdir()
    f1 = tmp_path / 'f1'
    f1.write_text('1')
    try:
        old_cwd = os.getcwd()
        os.chdir(tmp_path)
        yield tmp_path
    finally:
        os.chdir(old_cwd)


@pytest.mark.xfail
def test_ls():
    from e6 import ls
    assert sorted(repr(ls).split()) == ['d1', 'f1']


@pytest.mark.xfail
def test_ls_l():
    from e6 import ls, l
    lines = sorted(repr(ls -l).splitlines()[1:])
    assert lines[0].startswith('-') and lines[0].endswith('f1')
    assert lines[1].startswith('d') and lines[1].endswith('d1')


@pytest.mark.xfail
def test_wc_c_f1():
    from e6 import wc, c
    assert repr(wc -c < 'f1').strip() == '1'


@pytest.mark.xfail
def test_ls_l_wc_c():
    from e6 import ls, l, wc, c
    assert 50 <= int(repr(ls -l | wc -c)) <= 150
