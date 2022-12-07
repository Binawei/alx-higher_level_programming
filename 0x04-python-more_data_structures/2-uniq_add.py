#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique = set(my_list)
    unique_list = list(unique)
    total = 0
    num = 0
    while (num < len(unique_list)):
        total += unique_list[num]
        num += 1
    return total
