#!/usr/bin/python3

def uppercase(str):
    nstr = ''
    for k in str:
        if ord(k) in range(ord('a'), ord('z') + 1):
            nstr += chr(ord(k) - ord('a') + ord('A'))
        else:
            nstr += k

    print('{}'.format(nstr))
