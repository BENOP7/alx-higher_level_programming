#!/usr/bin/python3


def remove_char_at(str, n):
    string = ''
    i = 0

    while i < len(str):
        if i == n:
            continue
        else:
            string += str[i]
        i += 1

    return string
