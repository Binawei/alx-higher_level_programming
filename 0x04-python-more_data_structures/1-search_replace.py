#!/usr/bin/python3
def search_replace(my_list, search, replace):
    for i, elem in enumerate(my_list):
        if elem == search:
            my_list[i] = replace
    return my_list
