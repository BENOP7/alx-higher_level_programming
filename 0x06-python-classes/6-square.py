#!/usr/bin/python3
'''
    Implements a simple python class, Square
'''


class Square:
    '''
        A class having a single private attribute, size
    '''
    def __init__(self, size=0, position=(0, 0)):
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
        if type(position) is tuple and len(position) == 2 and
        type(position[0]) is int and type(position[1]) is int:
            self.__position = value
        else:
            raise TypeError('position must be a tuple of 2 positive integers')

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

    @property
    def position(self):
        '''
            the position of the square on the xy-plane
        '''
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is tuple and len(value) == 2 and
        type(value[0]) is int and type(value[1]) is int:
            self.__position = value
        else:
            raise TypeError('position must be a tuple of 2 positive integers')

    def area(self):
        '''
            returns the area of the square
        '''
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            for j in range(self.__size):
                print('#', end='')
            print()
