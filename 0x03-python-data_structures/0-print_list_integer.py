#!/usr/bin/python3
def print_list_integer(my_list=[]):
    for element in my_list:
        print("{:.0f}".format(element))

my_list = [1, 2, 89, 65, 4, 5]
print_list_integer(my_list)
