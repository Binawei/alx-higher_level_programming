#!/usr/bin/python3
"""
Module returns the dictionary description with a simple data structure
from JSON serialization of an object
"""
def class_to_json(obj):
    """returns the dictionary description of an obj"""

    result = {}
    if hasattr(obj, "__dict__"):
        result = obj.__dict__.copy()
    return result
