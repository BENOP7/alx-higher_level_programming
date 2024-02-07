#!/usr/bin/python3
'''
Python script that adds all arguments passed to it to a python
list
'''
import json
from sys import argv as args


filename = 'add_item.json'
my_list = []
arg_list = [args[i] for i in range(1, len(args))]

try:
    with open(filename, 'r', encoding='utf-8') as f:
        my_list = json.load(f)
    for arg in arg_list:
        my_list.append(arg)
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_list, f)
except Exception:
    for arg in arg_list:
        my_list.append(arg)
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_list, f)
