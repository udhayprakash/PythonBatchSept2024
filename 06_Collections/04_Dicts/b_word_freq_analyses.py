#!/usr/bin/python3
"""
Purpose: Test Frequency Analyses
"""
from pprint import pp

sentence = '''Python is a wonderful language.
we can solve any
computational problem with this language'''

# Character frequency analyses
frequency = {}
for each_char in sentence:
    # print(each_char)
    try:
        frequency[each_char] = frequency[each_char] + 1
    except KeyError:
        # print('No such key')
        frequency[each_char] = 1

# print(frequency)
pp(frequency)


# Method 2
frequency = {}
for each_char in sentence:
    if each_char in frequency: 
        # frequency[each_char] = frequency[each_char] + 1
        frequency[each_char] += 1
    else:
        frequency[each_char] = 1
pp(frequency)


# Method 3
frequency = {}
for each_char in sentence:
    existing_count = frequency.get(each_char)
    if existing_count:
        frequency[each_char] += 1
    else:
        frequency[each_char] = 1
pp(frequency)


# Method 4
frequency = {}
for each_char in sentence:
    if existing_count := frequency.get(each_char): # walrus operator
        frequency[each_char] += 1
    else:
        frequency[each_char] = 1
pp(frequency)


# Method 5
frequency = {}
for each_char in sentence:
    frequency.setdefault(each_char, 0)
    frequency[each_char] += 1
pp(frequency)


# Method 6
from collections import Counter

frequency = Counter(sentence)
pp(frequency)
print(type(frequency))

frequency = dict(frequency)
pp(frequency)
