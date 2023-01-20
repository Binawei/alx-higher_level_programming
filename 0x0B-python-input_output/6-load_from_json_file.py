#!/usr/bin/python3
"""
a function that creates an Object from a "JSON file�":
"""
import json
def load_from_json_file(filename):
    """creates an Object from a “JSON file”:
    args: filename: the file to create the object from
    """
    with open(filename, 'r', encoding="UTF-8") as f:
        return json.load(f)
