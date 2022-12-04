#!/usr/bin/python3
def no_c(my_string):
    #charcters to be removed stored in ch
    ch = ['c', 'C']
    #to filter out the characters
    filtered_char = filter(lambda item: item not in ch, my_string)
    my_string = ''.join(filtered_char)
    print(my_string)
