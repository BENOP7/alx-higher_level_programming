#!/usr/bin/python3

def safe_print_division(a, b):
    d = None
    try:
        d = a / b
    except ZeroDivisionError:
        return d
    finally:
        print('Inside result: {}'.format(d))

    return d
