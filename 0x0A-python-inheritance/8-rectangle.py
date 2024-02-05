#!/usr/bin/python3
'''
    This module contains ``Rectangle`` class that 
    inherits from the class ``BaseGeometry``
'''


class Rectangle(BaseGeometry):
    '''
    A quadrilateral (having four sides)
    '''
    def __init__(self, width, height):
        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height
