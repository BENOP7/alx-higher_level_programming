#!/usr/bin/python3
'''
This module contains the add_integer() function,
which adds two numbers and returns their sum
'''


def add_integer(a, b=98):
    '''
    Adds two integers and returns the sum
    '''
    if type(a) not in [int, float]:
        raise TypeError('a must be an integer')
    if type(b) not in [int, float]:
        raise TypeError('b must be an integer')
    a = int(a)
    b = int(b)
    return a + b
