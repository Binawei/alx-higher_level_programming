#!/usr/bin/python3
"""
a function that appends a string at the end of a text file (UTF8)
and returns the number of characters added:
"""
def append_write(filename="", text=""):
    """
    appends a string at the end of a text file (UTF8) and returns the
    number of characters added:
    args:
        -filename: the file to append the text
        -text: the text to be appended to the file
    """
    with open(filename, 'a') as f:
        return f.write(text)


nb_characters_added = append_write("file_append.txt", "This School is so cool!\n")
print(nb_characters_added)
