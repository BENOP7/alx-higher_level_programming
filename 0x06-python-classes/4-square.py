#!/usr/bin/python3
'''
    Implements a simple python class, Square
'''


class Square:
    '''
        A class having a single private attribute, size
    '''
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    @property
    def size(self):
        '''
            size property that holds the value of the square's side
        '''
        return self.__size

    @size.setter
    def size(self, value):
        '''
            sets the size property of the square
        '''
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        '''
            returns the area of the square
        '''
        return self.__size ** 2
