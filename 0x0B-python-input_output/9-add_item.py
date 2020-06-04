#!/usr/bin/python3
"""
script that adds all arguments to a Python list, and then save them to a file
"""


import json
from sys import argv

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

try:
    args = load_from_json_file("add.item.json")
except:
    args = []
for item in argv[1:]:
    args.append(item)
save_to_json_file(args, "add_item.json")
