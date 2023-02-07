#!/usr/bin/python3
"""
This module
write a function that reads a text file (UTF8) and prints it to stdout:
"""
def read_file(filename=""):
    """
    reads a text file (UTF8) and prints it to stdout
    """
    with open(filename) as a_file:
        line = a_file.read()
        print(line, end='')
