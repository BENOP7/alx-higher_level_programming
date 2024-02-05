#!/usr/bin/python3
'''
    This module contains a class ``BaseGeometry``
'''


class BaseGeometry:
    '''
    class BaseGeometry
    '''
    def area(self):
        '''
        instance method area
        '''
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        '''
        validates integers

        Arguments:
            name: name of the attribute
            value: value of the attribute
        '''
        if type(value) is not int:
            raise TypeError(name + ' must be an integer')
        if value <= 0:
            raise ValueError(name + ' must be greater than 0')
