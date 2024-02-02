#!/usr/bin/python3
'''
This module conatains an implementation of a Rectangle class
'''


class Rectangle:
    '''
    This class defines a rectangle having a width and a
    height
    '''
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        if type(width) is not int:
            raise TypeError('width must be an integer')
        if type(height) is not int:
            raise TypeError('height must be an integer')
        if width < 0:
            raise ValueError('width must be >= 0')
        if height < 0:
            raise ValueError('height must be >= 0')
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        '''
        returns the value of the width
        '''
        return self.__width

    @width.setter
    def width(self, value):
        '''
        sets the value of the rectangle's width
        '''
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        '''
        returns the value of the height
        '''
        return self.__height

    @height.setter
    def height(self, value):
        '''
        sets the value of the rectangle's height
        '''
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """
        public instance method to calculate area of rectangle
        Returns: area of rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        public instance method to calculate the perimeter of a rectangle
        Returns: perimeter of rectangle
        """
        if self.__width is 0 or self.__height is 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
            return string representation of a rectangle
        """
        rectangle = ""
        if self.__width is 0 or self.__height is 0:
            return rectangle

        for i in range(self.__height - 1):
            rectangle += "#" * self.__width + "\n"
        rectangle += "#" * self.__width

        return rectangle

    def __repr__(self):
        """
            returns a string representation of the rectangle to be
            able to recreate a new instance
        """
        rectangle = "Rectangle({}, {})".format(self.__width, self.__height)
        return rectangle

    def __del__(self):
        """
            properly deletes the instance of a class.
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
