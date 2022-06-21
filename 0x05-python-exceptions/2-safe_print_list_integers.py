#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    n = 0
    try:
        for i in range(0, x):
            try:
                e = int(my_list[i])
            except ValueError:
                continue
            print('{:d}'.format(e), end='')
            n += 1
    except IndexError:
        print()
        return n
    print()
    return n
