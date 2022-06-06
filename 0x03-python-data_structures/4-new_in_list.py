#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    mlist = []
    for a in my_list:
        if my_list.index(a) == idx:
            mlist.append(element)
        else:
            mlist.append(a)
    return mlist
