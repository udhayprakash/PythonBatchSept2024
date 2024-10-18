#!/usr/bin/python3
"""
Purpose: Getting Command-line arguments
"""
import sys

print("__file__", __file__)
print("sys.argv", sys.argv)


"""
 $ python b_command_line_args.py 
__file__ /workspaces/PythonBatchSept2024/10_Modules/02_sys/b_command_line_args.py
sys.argv ['b_command_line_args.py']
 $ python b_command_line_args.py asd
__file__ /workspaces/PythonBatchSept2024/10_Modules/02_sys/b_command_line_args.py
sys.argv ['b_command_line_args.py', 'asd']
 $ python b_command_line_args.py asd 213 True
__file__ /workspaces/PythonBatchSept2024/10_Modules/02_sys/b_command_line_args.py
sys.argv ['b_command_line_args.py', 'asd', '213', 'True']
 $ python b_command_line_args.py asd 213 True None ['1']
__file__ /workspaces/PythonBatchSept2024/10_Modules/02_sys/b_command_line_args.py
sys.argv ['b_command_line_args.py', 'asd', '213', 'True', 'None', '[1]']
 $  cd ..
$ python 02_sys/b_command_line_args.py 
__file__ /workspaces/PythonBatchSept2024/10_Modules/02_sys/b_command_line_args.py
sys.argv ['02_sys/b_command_line_args.py']
 $ cd ..
 $ python 10_Modules/02_sys/b_command_line_args.py 
__file__ /workspaces/PythonBatchSept2024/10_Modules/02_sys/b_command_line_args.py
sys.argv ['10_Modules/02_sys/b_command_line_args.py']


"""