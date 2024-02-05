#!/usr/bin/python3
'''
    This module contains ``inherits_from`` a function
    that checks if an object's class is a subclass class of
    a given class
'''


def inherits_from(obj, a_class):
    '''
         returns True if the object is an instance of a class
         that inherited directly or indirectly from a specified class
         otherwise False
    '''
    if obj.__class__ == a_class:
        return False
    return issubclass(obj.__class__, a_class)
