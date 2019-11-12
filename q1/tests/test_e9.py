from e9 import StandardOutput


def test_capture():
    with StandardOutput() as stdout:
        print('Hello, world!')
    assert stdout.value == 'Hello, world!\n'


def test_no_output(capsys):
    with StandardOutput():
        print('Dead men tell no tales')
    out, err = capsys.readouterr()
    assert out == ''
    assert err == ''
