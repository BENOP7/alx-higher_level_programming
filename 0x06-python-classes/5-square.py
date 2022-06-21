#!/usr/bin/python3

""" This module contains the class Square """


class Square:
    """ Square represents a square model """
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    def area(self):
        """ Return the area of the square """
        return self.__size ** 2

    @property
    def size(self):
        """ Get the size of the square """
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def my_print(self):
        """ Print the square using '#' """
        if self.__size:
            for i in range(self.__size):
                print('#' * self.__size)
        else:
            print()
