#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    r = None
    try:
        r = fct(*args)
        return r
    except Exception as e:
        print('Exception: {}'.format(e),
              file=sys.stderr)
        return r
