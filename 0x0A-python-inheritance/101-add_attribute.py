#!/usr/bin/python3
"""
This module a function that adds a new attribute to an object if its possible:
"""
def add_attribute(obj, name, value):
    """adds a new attribute to an object if it's possible:
    Args:
        - obj: object to add the attribute to
        - name: name of the attribute
        - value: value of the attribute to add
    """
    if not hasattr(obj, '__slots__') and not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    if hasattr(obj, '__slots__') and not hasattr(obj, name):
        raise TypeError("can't add new attribute")

    setattr(obj, name, value)
