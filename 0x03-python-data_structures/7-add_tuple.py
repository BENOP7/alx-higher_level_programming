#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    size_a = len(tuple_a)
    size_b = len(tuple_b)
    if size_a > 1 and size_b > 1:
        return tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]
    for i in range(2 - size_a):
        tuple_a += 0,
    for i in range(2 - size_b):
        tuple_b += (0,)
    return tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]
