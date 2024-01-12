#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return None
    best = list(a_dictionary)[0]
    for key in list(a_dictionary):
        if a_dictionary[key] > a_dictionary[best]:
            best = key
    return best
