#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list:
        my_list.reverse()
        for element in my_list:
            print("{:d}".format(element))


my_list = [1, 2, 3, 4, 5]
print_reversed_list_integer(my_list)
