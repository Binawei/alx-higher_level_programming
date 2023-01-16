#!/usr/bin/python3
""" a class MyList that inherits from list:"""
class MyList(list):
    """Mylist imherit from list class"""
    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""
        new_list = self[:]
        new_list.sort()
        print("{}".format(new_list))
