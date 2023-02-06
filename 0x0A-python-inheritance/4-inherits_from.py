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


a = True
if inherits_from(a, int):
    print("{} inherited from class {}".format(a, int.__name__))
if inherits_from(a, bool):
    print("{} inherited from class {}".format(a, bool.__name__))
if inherits_from(a, object):
    print("{} inherited from class {}".format(a, object.__name__))

