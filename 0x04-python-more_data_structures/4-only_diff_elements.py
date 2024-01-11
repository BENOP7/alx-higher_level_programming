#!/usr/bin/python3


def only_diff_elements(set_1, set_2):
    if set_1 is None or set_2 is None:
        return set()
    return set_1.difference(set_2).union(set_2.difference(set_1))
