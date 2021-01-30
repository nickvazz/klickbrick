from behave import given, then

import klickbrick.cli


@given('installed klickbrick')
def step_impl(context):
    print(klickbrick.cli.__file__)
    assert klickbrick.cli.__name__ == 'cli.py'
