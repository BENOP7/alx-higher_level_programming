#!/usr/bin/python3
'''
    This module contains ``Rectangle`` class that
    inherits from the class ``BaseGeometry``
'''

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''
    A quadrilateral (having four sides)
    '''
    def __init__(self, width, height):
        '''
        This is the constructor of the rectangle class
        '''
        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height

    def area(self):
        '''
        returns the area of the rectangle instance
        '''
        return self.__width * self.__height

    def __str__(self):
        '''
        Returns a string representation of the rectangle object
        '''
        return '[Rectangle] {:d}/{:d}'.format(self.__width, self.__height)
