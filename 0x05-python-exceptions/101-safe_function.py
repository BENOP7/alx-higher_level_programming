#!/usr/bin/python3

def safe_function(fct, *args):
    r = None
    try:
        r = fct(*args)
        return r
    except Exception as e:
        print('Exception: {}'.format(e))
        return r
