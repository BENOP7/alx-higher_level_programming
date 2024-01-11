#!/usr/bin/python3


def uniq_add(my_list=[]):
    total = 0
    if my_list is None:
        return total
    number_set = set(my_list)
    for n in number_set:
        total += n
    return total


if __name__ == '__main__':
    uniq_add([1, 2, 3])
