#!/usr/bin/python3
'''
This module contains the lazy_matrix_mul() function that
multiplies two matrices
'''
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    '''
    Multiplies m_a and m_b if they can be multiplied

    Arguments:
        m_a: first matrix
        m_b: second matrix
    '''
    a = np.array(m_a)
    b = np.array(m_b)
    return np.matmul(a, b)
