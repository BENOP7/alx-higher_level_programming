#!/usr/bin/python3

def no_c(my_string):
    new_s = ''.join(['' if c.lower() == 'c' else c for c in my_string])
    return new_s
