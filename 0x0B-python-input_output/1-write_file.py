#!/usr/bin/python3
"""Module 1-write_file.py.
writes a string to a text file (UTF8) and returns the number of characters written:
"""
def write_file(filename="", text=""):
    """writes a string to a text file (UTF8) and returns the number of characters written:
    args:
        -filename: name of the file
        -text: the texts to be written on the file
    """
    with open(filename, 'w', encoding='utf-8') as a_file:
        return a_file.write(text)
