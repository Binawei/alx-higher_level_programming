#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    over = len(my_list)
    insert = my_list.insert(idx, element)
    if idx < 0:
        return my_list
    elif idx > over:
        return my_list
    else:
        return insert
