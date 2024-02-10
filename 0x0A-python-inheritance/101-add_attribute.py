#!/usr/bin/python3
'''
This module contains a function add_attribute that adds an attribute
to an object
'''


def add_attribute(obj, attr, val):
    '''
    adds attribute 'attr' with value 'val' to obj
    '''
    if type(obj) is str or type(obj) is tuple:
        raise TypeError("can't add new attribute")
    if type(attr) is not str:
        raise TypeError("can't add new attribute")
    if hasattr(obj, attr):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, val)
