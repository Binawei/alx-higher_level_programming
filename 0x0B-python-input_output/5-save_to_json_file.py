#!/usr/bin/python3
"""
module 5-save_to_json_file.py
a function that writes an Object to a text file, using a JSON representation:
"""
import json

def save_to_json_file(my_obj, filename):
    """
    writes an Object to a text file, using a JSON representation:
    args:
        -my_obj: the object to write ti json file
        -filename: the file to write to
    """
    with open(filename, 'w') as a_file:
         return json.dump(my_obj, a_file)

