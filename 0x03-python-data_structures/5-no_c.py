#!/usr/bin/python3
def no_c(my_string):
    my_list = list(my_string)
    for ch in my_list:
        if ch == 'c' or ch == 'C':
            my_list.remove(ch)
    return "".join(my_list)
