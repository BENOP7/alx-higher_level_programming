#!/usr/bin/python3

def pow(a, b):
    i = 0
    r = 1
    if b > 0:
        while i < b:
            r *= a
            i += 1
    if b < 0:
        while i > b:
            r /= a
            i -= 1
    return r
