#!/usr/bin/python3
"""
Purpose: Demonstration of usage of help()
on python objects
"""

dozen = 12  # int
dozen = 12.3  # float
# dozen = None  # NoneType
# dozen = True  # bool
print(f"{type(dozen) =}")
print(f"{id(dozen)  =}")
print(f"{dozen      =}")

print(f"{dir(dozen) =}")

help(dozen)