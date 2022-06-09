#!/usr/bin/python3

def uniq_add(my_list=[]):
    myls = []

    if my_list:
        for elt in my_list:
            if my_list.count(elt) == 1:
                myls.append(elt)

    return myls
