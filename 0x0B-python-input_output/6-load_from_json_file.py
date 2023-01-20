#!/usr/bin/python3
""" Module that creates an object from a JSON file
"""
import json
def load_from_json_file(filename):
    """function tht creates an object from a JSON file:
    args:
        filename: the file to create the object from
    Raises:
        Exception: when the object can't be encoded
    """
    with open(filename, 'r', encoding="UTF-8") as f:
        return json.load(f)
