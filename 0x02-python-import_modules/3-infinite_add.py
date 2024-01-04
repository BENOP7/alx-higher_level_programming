#!/usr/bin/python3
from sys import argv as numbers


if __name__ == '__main__':
    sum = 0
    for i in range(1, len(numbers)):
        sum += int(numbers[i])

    print(sum)
