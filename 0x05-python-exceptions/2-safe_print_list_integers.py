#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    n = i = 0
    while n != x
        try:
            e = int(my_list[i])
        except ValueError:
            i += 1
            continue
        print('{:d}'.format(e), end='')
        n += 1
        i += 1
    print()
    return n
