#!/usr/bin/python
"""
Purpose: Exception Handling
"""
try:
    num1 = int(input("Enter an integer:"))
    num2 = int(input("Enter an integer:"))  # 12.3 -- TypeError
except Exception as ex:
    print(f"{ex =}")
    print("Please enter integers only")
else:
    try:
        division = num1 / num2  # ZeroDivisionError
    except Exception as ex1:
        print(f"\t{ex1 =}")
        print("\tDenominator cant be zero")
    else:
        print(f"\t{division = }")
    finally:
        print('\tfinally -- inside')
finally:
    print('finally -- outside')


# NOTE: Its recommended to place statements which may be prone to exceptions
