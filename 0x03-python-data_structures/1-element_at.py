#!/usr/bin/python3
def element_at(my_list, idx):
    over = len(my_list)
    if idx < 0:
        return None
    elif idx >= over:
        return None
    else:
        return my_list.pop(idx)
