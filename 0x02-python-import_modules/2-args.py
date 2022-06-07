#!/usr/bin/python3

from sys import argv

if __name__ == '__main__':
    ac = len(argv)
    statement = '{:d} argument'.format(ac - 1)
    if ac != 2:
        statement = 's'.join([statement, ''])
    statement = ':'.join([statement, '']) if ac != 1\
else '.'.join([statement, ''])
    print(statement)

    for argument in argv:
        if argv.index(argument) != 0:
            print('{:d}: {}'.format(argv.index(argument), argument))
