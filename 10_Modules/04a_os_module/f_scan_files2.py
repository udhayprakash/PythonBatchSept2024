"""
Problem: List all the Python and jupyer notebooks. 
    Give the share of each. 
    Exclude other file types
"""

import os
from pprint import pp
from typing import List



# print(f'curr directory         : {os.getcwd()}')
# print(f'files in curr directory: {os.listdir()}')

# print(f'par directory         : {os.getcwd()}')
# print(f'files in par directory: {os.listdir(os.pardir)}')


# print(os.walk(os.curdir))
# # <generator object walk at 0x75ee15e34040>

# walk_object = os.walk(os.pardir)
# pp(next(walk_object))
# print()
# pp(next(walk_object))
# print()

# def scan_files(path_to_search: str, extensions: str = '.py') -> List[str]:
#     file_names = []
#     for each_dir, list_of_dirs, list_of_files in os.walk(path_to_search):
#         for each_file in list_of_files:
#             _, extension = os.path.splitext(each_file)
#             if extension == extensions:
#                 file_names.append(each_file)

#     return file_names

# print('python file =', scan_files('.'))

# # relative paths
# print('python file =', scan_files('../../..'))


def scan_files(path_to_search: str, extensions: str = '.py') -> int:
    file_names_count = 0
    for each_dir, list_of_dirs, list_of_files in os.walk(path_to_search):
        for each_file in list_of_files:
            _, extension = os.path.splitext(each_file)
            if extension == extensions:
                file_names_count += 1
    return file_names_count

# print('python file =', scan_files('.'))

# # relative paths
# print('python file =', scan_files('..'))
# print('python file =', scan_files('../..'))
# print('python file =', scan_files('../../..'))


"""
python file = 5
python file = 7
python file = 103
python file = 1036
@udhayprakash ➜ /workspaces/PythonBatchSept2024/10_Modules/02_sys (class23) $ python ../02_sys/f_scan_files2.py 
python file = 5
python file = 7
python file = 103
python file = 1036
@udhayprakash ➜ /workspaces/PythonBatchSept2024/10_Modules/02_sys (class23) $ cd ..
@udhayprakash ➜ /workspaces/PythonBatchSept2024/10_Modules (class23) $ python 02_sys/f_scan_files2.py 
python file = 7
python file = 103
python file = 1036
python file = 41312

"""
# absolute paths
print('python file =', scan_files('/workspaces/PythonBatchSept2024/10_Modules/02_sys'))
print('python file =', scan_files('/workspaces/PythonBatchSept2024/10_Modules'))
print('python file =', scan_files('/workspaces/PythonBatchSept2024'))


"""
@udhayprakash ➜ /workspaces/PythonBatchSept2024/10_Modules (class23) $ python 02_sys/f_scan_files2.py 
python file = 5
python file = 7
python file = 103
@udhayprakash ➜ /workspaces/PythonBatchSept2024/10_Modules (class23) $ cd 02_sys/
@udhayprakash ➜ /workspaces/PythonBatchSept2024/10_Modules/02_sys (class23) $ python f_scan_files2.py 
python file = 5
python file = 7
python file = 103
@udhayprakash ➜ /workspaces/PythonBatchSept2024/10_Modules/02_sys (class23) $ cd ../
@udhayprakash ➜ /workspaces/PythonBatchSept2024/10_Modules (class23) $ cd ../
@udhayprakash ➜ /workspaces/PythonBatchSept2024 (class23) $ python 10_Modules/02_sys/f_scan_files2.py 
python file = 5
python file = 7
python file = 103
"""

# assignment -repat the same.. give the percentage distrobution of each extension
# HINT: dict, 