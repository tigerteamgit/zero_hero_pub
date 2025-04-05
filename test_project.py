from mylib.calc import *
from calCLI import cli
from click.testing import CliRunner
import pytest

#create fixture to invoke the runner to setup each instance, ie "add" "sub" "mul" "div" "pow"
@pytest.fixture
def cli_runner():
    return CliRunner()

def test_add(runner):
    result = cli_runner.invoke(cli, ['add', '1', '2'])
    assert result.exit_code == 0

def test_sub():
    assert sub(2, 1) == 1
    assert sub(-1, 1) == -2
    assert sub(-1, -1) == 0

def test_mul():
    assert mul(2, 3) == 6
    assert mul(-1, 1) == -1
    assert mul(-1, -1) == 1

def test_div():
    assert div(6, 3) == 2
    assert div(-1, 1) == -1
    assert div(-1, -1) == 1
    try:
        div(1, 0)
    except ValueError:
        pass
    else:
        assert False

def test_pow():
    assert pow(6, 3) == 216
    assert pow(-1, 1) == -1
    assert pow(0, 0) == 1
    assert pow(0, 1) == 0
    assert pow(1, 0) == 1
    assert pow(1, 1) == 1