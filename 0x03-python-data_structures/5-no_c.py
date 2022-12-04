#!/usr/bin/python3
def no_c(my_string):
    ch = ['c', 'C']
    filtered_char = filter(lambda item: item not in ch, my_string)
    my_string = ''.join(filtered_char)
    print(my_string)
