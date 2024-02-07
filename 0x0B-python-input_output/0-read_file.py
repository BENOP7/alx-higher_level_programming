#!/usr/bin/python3
'''
This module contains ``read_file`` function
'''


def read_file(filename=''):
    '''
    Reads the content of a file and prints it to stdout
    '''
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            print(line, end='')
