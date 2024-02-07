#!/usr/bin/python3
'''
This module contains ``append_write`` function
'''


def append_write(filename='', text=''):
    '''
    appends the content of a string to the text file
    '''
    count = 0
    with open(filename, 'a', encoding='utf-8') as f:
        if type(text) is str:
            count = f.write(text)
    return count
