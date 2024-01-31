#!/usr/bin/python3
'''
This module implements a function for matrix
multiplication
'''


def matrix_mul(m_a, m_b):
    '''
    multiplies two matrices if they are compatible
    for multiplication

    Arguments:
        m_a: first matrix
        m_b: second matrix
    '''
    if type(m_a) is not list:
        raise TypeError('m_a must be a list')
    if len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    if type(m_b) is not list:
        raise TypeError('m_b must be a list')
    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")

    for row in m_a:
        if type(row) is not list:
            raise TypeError('m_a must be a list of lists')
    for row in m_b:
        if type(row) is not list:
            raise TypeError('m_b must be a list of lists')
    if len(m_a) == 1 and len(m_a[0]) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 1 and len(m_b[0]) == 0:
        raise ValueError("m_b can't be empty")
    for row in m_a:
        for a in row:
            if type(a) not in [int, float]:
                raise TypeError('m_a should contain only integers or floats')
    for row in m_b:
        for a in row:
            if type(a) not in [int, float]:
                raise TypeError('m_b should contain only integers or floats')
    cols_a = len(m_a[0])
    cols_b = len(m_b[0])
    for row in m_a:
        if len(row) != cols_a:
            raise TypeError('each row of m_a must be of the same size')
    for row in m_b:
        if len(row) != cols_b:
            raise TypeError('each row of m_b must be of the same size')

    if len(m_b) != cols_a:
        raise ValueError("m_a and m_b can't be multiplied")

    prod = [[0 for i in range(len(m_b[0]))] for j in range(len(m_a))]
    for i in range(len(m_a)):
        for j in range(cols_b):
            for k in range(len(m_b)):
                prod[i][j] += m_a[i][k] * m_b[k][j]
    return prod
