#!/usr/bin/python3
"""
Purpose: To display the asterisk's in a half-diamond pattern
"""

# half-diamond
for num in range(0, 10, 1):
    print(num * "*")  # string repetition operator

for num in range(9, -1, -1):
    print(num * "*")  # string repetition operator
 

for num in range(0, 10, 1):
   print( (9 - num) * ' ' + num * '*')

for num in range(9, -1, -1):
   print( (9 - num) * ' ' + num * '*')

"""
Assignment:full diamond problem
       *
      ***
     *****
    *******
   *********
  ***********
 *************
***************
 *************
  ***********
    *******
     *****
      ***
       *

       using both for loop and while loop seperately
"""