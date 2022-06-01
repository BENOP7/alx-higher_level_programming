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
        if b < -5:
            r = r - 10**-36
    return r
