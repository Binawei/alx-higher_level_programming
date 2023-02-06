#!/usr/bin/python3
"""This moduule writes
a function that returns the list of available attributes
and methods of an object:"""
def lookup(obj):
    """the function to return the list usin the dir() function"""
    return dir(obj)
