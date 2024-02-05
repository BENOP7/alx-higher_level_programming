#!/usr/bin/python3
'''
    In this module is found a function ``lookup`` that
    returns the available attributes and methods of a class
'''


def lookup(obj):
    '''
        Returns available attributes and methods of obj

        Arguments:
            obj: the object
    '''
    return dir(obj)
