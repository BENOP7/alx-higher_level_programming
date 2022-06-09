#!/usr/bin/python3

def uniq_add(my_list=[]):

    r = my_list.copy()
    if r:
        r = list(set())

    return sum(r)
