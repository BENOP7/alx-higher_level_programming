#!/usr/bin/python3


def max_integer(my_list=[]):
    if len(my_list) < 1:
        return None
    if len(my_list) == 1:
        return my_list[0]
    largest = my_list[0]
    for n in my_list[1:]:
        if n > largest:
            largest = n
