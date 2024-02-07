#!/usr/bin/python3
'''
This module contains ``write_file`` function
'''


def write_file(filename='', text=''):
    '''
    Writes the content of a string to the text file
    '''
    with open(filename, 'w', encoding='utf-8') as f:
        if type(text) is str:
            f.write(text)
