#!/usr/bin/python3
'''
This module contains MyInt class a kind of integer
'''


class MyInt(int):
    '''
    This is a rebel kind of integer class with operations == and !=
    malfunctioning
    '''
    def __eq__(self, other):
        if type(other) is type(self) or issubclass(self.__class__, int):
            if self.__int__() == other.__int__():
                return False
            return True
        super().__eq__(other)

    def __ne__(self, other):
        if type(other) is type(self) or issubclass(self.__class__, int):
            if self.__int__() == other.__int__():
                return True
            return False
        super().__eq__(other)
