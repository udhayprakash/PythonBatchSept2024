"""
Purpose: Reading(Parsing) CSV using csv module
"""
import csv
from pprint import pp
# print(dir(csv))

with open('my_file.csv', 'r') as fh:
    # data = fh.read()
    file_content = csv.reader(fh, delimiter=',')
    # print(file_content)

    # pp(list(file_content))


    # To skip the header

    # for each_line in file_content[1:]:
    # TypeError: '_csv.reader' object is not subscriptable

    next(file_content)
    
    names = []
    for each_line in file_content:
        # print(each_line)
        name = each_line[1]
        names.append(name)

print(names)
