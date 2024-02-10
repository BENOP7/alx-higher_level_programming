#!/usr/bin/python3
'''
This module contains a ``Square`` class
That inherits from ``Rectangle``
'''

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''
    This class implements a square plane with a side
    It inherits the ``Rectangle`` class
    '''
    def __init__(self, size):
        Square.integer_validator('size', size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        '''
        Calculates the area of the square and returns it
        '''
        return self.__size ** 2
