#!/usr/bin/python3
"""
a function that reads a text file (UTF8) and prints it to stdout:
"""
def read_file(filename=""):
    """
    reads a text file (UTF8) and prints it to stdout
    """
    with open(filename) as f:
        line = f.read()
        print(line, end='')
