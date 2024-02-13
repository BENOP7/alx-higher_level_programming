#!/usr/bin/python3
'''
This module contains the rectangle class that inherits
from the Base class
'''
from models.base import Base


class Rectangle(Base):
    '''
    The rectangle is a 2D quadrilateral (geometry with four sides)
    The Rectangle class is a model of this geometric shape
    '''
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        if type(width) is not int:
            raise TypeError('width must be an integer')
        if width <= 0:
            raise ValueError('width must be > 0')
        self.__width = width
        if type(height) is not int:
            raise TypeError('height must be an integer')
        if height <= 0:
            raise ValueError('height must be > 0')
        self.__height = height
        if type(x) is not int:
            raise TypeError('x must be an integer')
        if x < 0:
            raise ValueError('x must be >= 0')
        self.__x = x
        if type(y) is not int:
            raise TypeError('y must be an integer')
        if y < 0:
            raise ValueError('y must be >= 0')
        self.__y = y

    @property
    def width(self):
        '''
        Gets the value of the width
        '''
        return self.__width

    @width.setter
    def width(self, value):
        '''
        Validates and sets the value of width
        '''
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        '''
        Gets the value of the height
        '''
        return self.__height

    @height.setter
    def height(self, value):
        '''
        Validates and sets the value of
        '''
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        '''
        Gets the value of the x
        '''
        return self.__x

    @x.setter
    def x(self, value):
        '''
        Validates and sets the value of x
        '''
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        '''
        Gets the value of the y
        '''
        return self.__y

    @y.setter
    def y(self, value):
        '''
        Validates and sets the value of y
        '''
        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        '''
        returns the area of the geometry (rectangle)
        '''
        return self.__width * self.__height

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
                setattr(self, k, v)
            return
        self.id = args[0]
        if n > 1:
            self.width = args[1]
        if n > 2:
            self.height = args[2]
        if n > 3:
            self.x = args[3]
        if n > 4:
            self.y = args[4]

    def to_dictionary(self):
        '''
        returns a dictionary containing all the instance attributes of the
        object
        '''
        prefix = '_{}__'.format(self.__class__.__name__)
        obj_dict = {}

        for key, value in self.__dict__.items():
            if prefix in key:
                obj_dict[key.replace(prefix, '')] = value
            else:
                obj_dict[key] = value
        return obj_dict

    def __str__(self):
        return '[{}] ({:d}) {:d}/{:d} - {:d}/{:d}'.format(
                self.__class__.__name__,
                self.id,
                self.__x, self.__y,
                self.__width, self.__height)
