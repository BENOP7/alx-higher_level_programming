#!/usr/bin/python3
'''
This module contains the rectangle class that inherits
from the Base class
'''
from base import Base


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
    def (self, value):
        '''
        Validates and sets the value of y
        '''
        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value
