#!/usr/bin/python3
"""
Purpose: String slicing operations
"""

# P   y  t  h  o n     P r o g  r  a  m  m  i  n  g
# 0   1  2  3  4 5  6  7 8 9 10 11 12 13 14 15 16 17   - forward indexing
# -18                                      -3 -2 -1    - reverse indexing
language = "Python Programming"
print("language       :", language)

# indexing
print("language[0]    :", language[0])
print()

# Slicing
print("String Slicing")                     # [start_index: final_index]
print("language[0:11] :", language[0:11])  # Python Prog
print("language[5:17] :", language[5:17])  # n Programmin
print("language[7:10] :", language[7:10])  # Pro

# NOTE: In python, it doesn't include the last value, in a boundary condition.
print()
print("language[0:5]  :", language[0:5])  # Pytho
print("language[0:6]  :", language[0:6])  # Python


print()
print("language[7:18] :", language[7:18])   # Programming
print("language[7:999]:", language[7:999])  # 999 index isn't present
print("language[45:87]:", language[45:87])  # indexes are not present

