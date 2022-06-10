#!/usr/bin/python3

def complex_delete(a_dictionary, value):

    if value not in a_dictionary.values():
        return a_dictionary

    delete = []
    for k, v in a_dictionary.items():
        if v == value:
            keys_to_delete.append(k)

    for k in keys_to_delete:
        del a_dictionary[]

    return a_dictionary
