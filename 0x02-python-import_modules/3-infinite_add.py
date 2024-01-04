#!/usr/bin/python3
from sys import argv as numbers


if __name__ == '__main__':
    first = 0
    second = 0
    if len(numbers) == 3:
        first = int(numbers[1])
        second = int(numbers[2])

    print(first + second)
