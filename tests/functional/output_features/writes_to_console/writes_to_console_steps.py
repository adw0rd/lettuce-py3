import sys

from lettuce import step

@step('When I write to stdout')
def write_stdout(step):
    print("Badger", file=sys.stdout)

@step('When I write to stderr')
def write_stderr(step):
    print("Mushroom", file=sys.stderr)

@step('Then I am happy')
def happy(step):
    pass
