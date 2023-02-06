#!/usr/bin/python3
"""
This module is a function that returns True if the object is an
instance of a class that it inherited directly or indirecly
"""
def inherits_from(obj, a_class):
    """
    returns True if the object is an instance of a class that
    inherited directly or indirectly from a specified class
    otherwise false.
    args:
        obj: the subclass
        a_class: the class to he inherited from
    """
    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    else:
        return False
