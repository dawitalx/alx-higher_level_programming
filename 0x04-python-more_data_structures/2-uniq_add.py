#!/usr/bin/python3

def uniq_add(my_list=[]):
    new_list = set(my_list)
    total = 0
    for x in new_list:
        total += x
    return (total)
