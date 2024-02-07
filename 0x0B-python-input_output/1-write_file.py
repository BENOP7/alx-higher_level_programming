#!/usr/bin/python3
'''
This module contains ``write_file`` function
'''


def write_file(filename='', text=''):
    '''
    Writes the content of a string to the text file
    '''
    count = 0
    with open(filename, 'w', encoding='utf-8') as f:
        if type(text) is str:
            count = f.write(text)
    return count
