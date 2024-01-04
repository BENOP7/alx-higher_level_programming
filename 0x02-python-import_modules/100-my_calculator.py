#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv as av

if __name__ == '__main__':
    if len(av) != 4:
        print('Usage: {:s} <a> <operator> <b>'.format(av[0]))
        quit(1)
    ops = ['+', '-', '*', '/']
    a = int(av[1])
    b = int(av[3])
    op = av[2]

    if op not in ops:
        print("Usage: {} <a> <operator> <b>".format(av[0]))
        quit(1)
    if op == '+':
        print('{:d} {} {:d} = {:d}'.format(a, op, b, add(a, b)))
    elif op == '-':
        print('{:d} {} {:d} = {:d}'.format(a, op, b, sub(a, b)))
    elif op == '*':
        print('{:d} {} {:d} = {:d}'.format(a, op, b, mul(a, b)))
    elif op == '/':
        print('{:d} {} {:d} = {:d}'.format(a, op, b, div(a, b)))
