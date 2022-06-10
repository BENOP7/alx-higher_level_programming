#!/usr/bin/python3


def weight_average(my_list=[]):

    if my_list == []:
        return 0

    tot = sum(list(map(lambda x: x[0] * x[1], my_list)))
    weight_sum = sum(list(map(lambda x: x[1], my_list)))
    avg = tot / weight_sum

    return avg
