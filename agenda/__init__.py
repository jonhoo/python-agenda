from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from builtins import (  # NOQA
         bytes, dict, int, list, object, range, str,
         ascii, chr, hex, input, next, oct, open,
         pow, round, super,
         filter, map, zip)

from termcolor import colored


def section(name):
    print('{} {}'.format(
        colored("::", 'blue', attrs=['bold']),
        colored(name, attrs=['bold'])
        )
    )


def task(name):
    print('{} {}'.format(
        colored("==>", 'green', attrs=['bold']),
        colored(name, attrs=['bold'])
        )
    )


def subtask(name):
    print('{} {}'.format(
        colored("  ->", 'blue', attrs=['bold']),
        colored(name, attrs=['bold'])
        )
    )


def failure(name):
    print('{} {}'.format(
        colored("==> ERROR:", 'red', attrs=['bold']),
        colored(name, attrs=['bold'])
        )
    )


def subfailure(name):
    print('{} {}'.format(
        colored("  ->", 'red', attrs=['bold']),
        colored(name, 'red', attrs=['bold'])
        )
    )


def prompt(name):
    print('{} {}'.format(
        colored("==>", 'yellow', attrs=['bold']),
        colored(name, attrs=['bold'])),
        end=""
    )


def subprompt(name):
    print('{} {}'.format(
        colored("  ->", 'yellow', attrs=['bold']),
        colored(name, attrs=['bold'])),
        end="")
