#!/usr/bin/python3
'''
The module contains the base model for all other classes
'''


class Base:
    '''
    base class for other classes
    '''
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects