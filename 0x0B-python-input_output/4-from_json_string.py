#!/usr/bin/python3
"""
module 4-from_json_string.py
Write a function that returns an object (Python data structure)
represented by a JSON string:
"""
import json

def from_json_string(my_str):
    """
    returns an object (Python data structure) represented by a JSON string:
    args:
        -my_str: the string to be retunred from json format
    """

    return json.loads(my_str)
