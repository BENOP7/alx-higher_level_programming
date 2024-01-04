#!/usr/bin/python3
from sys import argv


if __name__ == "__main__":
    n = len(argv)
    print(n - 1, "argument:" if n == 2 else "arguments:")

    for i in range(1, n):
        print(str(i) + ': ' + argv[i])
