#!/usr/bin/python3


def fizzbuzz():
    for k in range(1, 100 + 1):
        if k % 3 == 0 and k % 5 == 0:
            print('FizzBuzz', end=' ')
        elif k % 3 == 0:
            print('Fizz', end=' ')
        elif k % 5 == 0 and k == 100:
            print('Buzz', end=' ')
        elif k % 5 == 0:
            print('Buzz', end=' ')
        else:
            print('{:d}'.format(k), end=' ')
