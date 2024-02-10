#!/usr/bin/python3
'''
This module contains MyInt class a kind of integer
'''


class MyInt(int):
    '''
    This is a rebel kind of integer class with operations == and !=
    malfunctioning
    '''
    def __eq__(self, other):
        return self != other

    def __ne__(self, other):
        return self == other
