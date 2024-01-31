#!/usr/bin/python3
'''
    This module contains the function `text_indentation`

'''


def text_indentation(text):
    '''
        Indents text after '.', '?', or ':'

        Args:
            text - contains the string of text
    '''
    if not isinstance(text, str):
        raise TypeError('text must be a string')

    if (len(text) == 1 and text[0] == ' '):
        print(text[0], end='')
        return

    for i in range(len(text)):
        if i > 0 and text[i - 1] in ['.', '?', ':']:
            while text[i] in ['\t', ' ', '\n']:
                i += 1
            if text[i - 1] in ['\t', ' ', '\n']:
                continue
        print(text[i], end='')
        if text[i] in ['.', '?', ':']:
            print('\n')
