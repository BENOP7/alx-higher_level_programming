#!/usr/bin/python3
'''
    This module contains ``is_kind_of_class`` a function
    that checks if two objects are having a common
    class
'''


def is_same_class(obj, a_class):
    '''
         returns True if the object is exactly an instance of
         the specified class ; otherwise False
    '''
    return isinstance(obj, a_class)
