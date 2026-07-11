#!/usr/bin/python3
"""Script that adds all arguments to a Python list, then saves it as JSON."""
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    list_items = load_from_json_file("add_item.json")
except Exception:
    list_items = []

list_items.extend(sys.argv[1:])

save_to_json_file(list_items, "add_item.json")
