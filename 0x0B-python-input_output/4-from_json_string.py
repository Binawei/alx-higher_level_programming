#!/usr/bin/python3
import json
"""
a function that returns an object (Python data structure)
represented by a JSON string:
"""
def from_json_string(my_str):
    """
    returns an object (Python data structure) represented by a JSON string:
    args:
        -my_str: string to be returned
    """
    return json.loads(my_str)

