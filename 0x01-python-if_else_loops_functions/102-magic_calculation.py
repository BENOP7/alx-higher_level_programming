#!/usr/bin/python3


def magic_calculation(a, b, c):
    if a < b:
        return c
    if c > b:
        return b + a
    return a * b - c
