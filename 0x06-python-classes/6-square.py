#!/usr/bin/python3

""" This module contains the class Square """


class Square:
    """ Square represents a square model """
    def __init__(self, size=0, position=(0, 0)):
        if not (isinstance(size, int)):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.__position = position

    def area(self):
        """ Return the area of the square """
        return self.__size ** 2

    @property
    def size(self):
        """ Get the size of the square """
        return self.__size

    @property
    def position(self):
        """ Returns the position of the square """
        return self.__position

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        if type(value) == tuple and len(value) == 2:
            if isinstance(value[0], int) and isinstance(value[-1], int):
                if value[0] >= 0 and value[-1] >= 0:
                    self.__position = position
        else:
            raise TypeError('position must be a tuple of 2 positive integers')

    def my_print(self):
        """ Print the square using '#' """
        if self.__size:
            print('\n' * self.position[-1], end='')
            for i in range(self.__size):
                print(' ' * self.position[0] + '#' * self.__size)
        else:
            print()
