#!/usr/bin/python3
'''
    Implements a magic class
'''
import math


class MagicClass:
    '''
        A class that implements special calculations
    '''
    def __init__(self, radius=0):
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        '''
            calculate the area and returns it
        '''
        return self.__radius ** 2 * math.pi

    def circumference(self):
        '''
            returns the circumference
        '''
        return 2 * math.pi * self.__radius
