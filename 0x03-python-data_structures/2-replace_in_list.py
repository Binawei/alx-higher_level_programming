#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    over = len(my_list)
    if idx < 0:
        return my_list
    elif idx >= over:
        return my_list
    else:
        return my_list.insert(idx, element)
