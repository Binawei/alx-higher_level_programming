#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    biggest_number = None
    for number in my_list:
        if biggest_number is None or biggest_number < number:
            biggest_number = number
    return biggest_number
