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
        if type(position) is tuple and len(position) == 2:
            if type(position[0]) is int and type(position[1]) is int:
                if position[0] >= 0 and position[1] >= 0:
                    self.__position = position
                else:
                    raise TypeError('position must be a tuple of 2 positive \
integers')
            else:
                raise TypeError('position must be a tuple of 2 positive \
integers')
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
        '''
            changes the value of the position of the square
        '''
        if type(value) is tuple and len(value) == 2:
            if type(value[0]) is int and type(value[1]) is int:
                if value[0] >= 0 and value[1] >= 0:
                    self.__position = value
                else:
                    raise TypeError('position must be a tuple of 2 positive \
integers')
            else:
                raise TypeError('position must be a tuple of 2 positive \
integers')
        else:
            raise TypeError('position must be a tuple of 2 positive integers')

    def area(self):
        '''
            returns the area of the square
        '''
        return self.__size ** 2

    def my_print(self):
        '''
            print the square using # characters based on the position too
        '''
        if self.__size == 0:
            print()
            return
        if self.__position[1] > 0:
            for n in range(self.__position[1]):
                print()
        for i in range(self.__size):
            for j in range(self.__size):
                if j == 0:
                    print(''.join([' ' for e in range(self.__position[0])]),
                          end='')
                print('#', end='')
            print()
