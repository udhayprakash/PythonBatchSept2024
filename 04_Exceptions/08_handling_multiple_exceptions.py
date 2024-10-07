#!/usr/bin/python3
"""
Purpose: Handling multiple exceptions together


In python 2,
    input() --- eval() builtin functions is used
    raw_input() -- will take anytihng as string

In python 3, 
    input()  --- raw_input is renamed as input() 
             -- will take anytihng as string


eval() and exec()
"""
try:
    expression = eval(input("Enter an expression:"))
except KeyboardInterrupt as ex1:
    print("YOU STOPPED WITH KEYBOARD INTERRUPT", ex1)
except (ZeroDivisionError, SyntaxError, TypeError) as ex3:
    print(f"Either zerodivision or syntax issue, or typing error occured:{ex3}")
except Exception as ex:
    print(f"Unhandled exception: {ex=}")
else:
    print(f"{expression =}")


"""
In [1]: eval('23')
Out[1]: 23

In [2]: eval('23.324')
Out[2]: 23.324

In [3]: eval('True')
Out[3]: True

In [4]: eval('None')

In [5]: eval('1+2432')
Out[5]: 2433

In [6]: eval('1+2432-232*23 + (3.2112312 + 4)')
Out[6]: -2895.7887688

"""