from klickbrick import __version__
from klickbrick.cli import main


def test_hello_subcommand():
    result = main(['hello'])

    assert result == "Hello World"

def test_hello_subcommand_with_name_flag():
    result = main(['hello', '--name', 'bill'])

    assert result == "Hello bill"


def test_version():
    assert __version__ == '0.1.0'
