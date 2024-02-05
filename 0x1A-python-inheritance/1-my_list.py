#!/usr/bin/python3
'''
    This module contains the class ``MyList``
    which inherits from the ``list`` class
'''


class MyList(list):
    '''
        a list type which inherits from ``list``
    '''
    def print_sorted(self):
        '''
            prints the list in sorted order
        '''
        cpy_list = self.copy()
        cpy_list.sort()
        print(cpy_list)
