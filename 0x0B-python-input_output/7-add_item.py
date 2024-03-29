#!/usr/bin/python3
""" Module adds all arguments to a python list, and save them to a file
"""
import sys
import os.path
import json

save_file = __import__('5-save_to_json_file').save_to_json_file
load_file = __import__('6-load_from_json_file').load_from_json_file

my_list = []
if os.path.exists("add_item.json"):
    my_list = load_file("add-item.json")

for argument in sys.argv[1:]:
    my_list.append(argument)

save_file(my_list, "add_item.json")
