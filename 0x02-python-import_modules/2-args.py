#!/usr/bin/python3
from sys import argv


if __name__ == "__main__":
    n = len(argv) - 1
    print(n, "argument:" if n == 1 else "arguments" + ('.' if n == 0 else ':'))

    for i in range(1, n + 1):
        print(str(i) + ': ' + argv[i])
