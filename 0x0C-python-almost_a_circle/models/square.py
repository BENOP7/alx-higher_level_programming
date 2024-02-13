#!/usr/bin/python3
'''
This module contains the square class that inherits
from ``Rectangle`` class
'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''
    The Square is a 2D quadrilateral (a kind of rectangle with all sides equal)
    The Rectangle class is a model of this geometric shape
    '''
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        '''
        retudns the value of the size (width or height)
        '''
        return self.width

    @size.setter
    def size(self, value):
        '''
        sets the value of the width and height to the same value
        '''
        self.width = value
        self.height = value

    def display(self):
        '''
        prints a representation of the rectangle using '#' character
        '''
        x = self.__x
        y = self.__y
        intercept = '\n' * y
        print(intercept, end='')

        for i in range(self.__height):
            print(' ' * x, end='')
            print('#' * self.__width)

    def update(self, *args, **kwargs):
        '''
        updates the attributes of the rectangle instance
        '''
        n = len(args)
        if n == 0:
            for k, v in kwargs.items():
                if k == 'size':
                    setattr(self, 'width', v)
                    setattr(self, 'height', v)
                else:
                    setattr(self, k, v)
            return
        self.id = args[0]
        if n > 1:
            self.width = args[1]
            self.height = args[1]
        if n > 2:
            self.x = args[2]
        if n > 3:
            self.y = args[3]

    def __str__(self):
        return '[{}] ({:d}) {:d}/{:d} - {:d}'.format(
                self.__class__.__name__,
                self.id,
                self.x, self.y,
                self.width)
