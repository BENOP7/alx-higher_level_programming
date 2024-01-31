#!/usr/bin/python3
'''
This module contains the function `matrix_divided` that divides
a matrix by a constant (int or float)
'''


def matrix_divided(matrix, div):
    '''
        matrix_divided divides a matrix by a constant div and returns the
        resulting matrix
        check an empty matrix ([[]])
    '''
    if type(div) not in [int, float]:
        raise TypeError('div must be a number')
    if type(matrix) is list:
        if len(matrix) == 0:
            raise TypeError('matrix must be a matrix (list of lists) \
of integers/floats')
        for row in matrix:
            if type(row) is not list:
                raise TypeError('matrix must be a matrix (list of lists) \
of integers/floats')
            for n in row:
                if type(n) not in [int, float]:
                    raise TypeError('matrix must be a matrix (list of lists) \
of integers/floats')
        size = len(matrix[0])
        for row in matrix:
            if len(row) != size:
                raise TypeError('Each row of the matrix must have the same \
size')
        result = [[0 for i in range(size)] for row in range(len(matrix))]
        for row in range(len(matrix)):
            for i in range(size):
                result[row][i] = round(matrix[row][i] / div, 2)
        return result
    raise TypeError('matrix must be a matrix (list of lists) \
of integers/floats')
    return None
