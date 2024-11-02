"""
Purpose: demo formateed code, as per pylint
"""

# Detecting unused variables


def my_function():
    """about the my_function() function"""
    unused_variable = 10


# Enforcing naming conventions
INVALID_VARIABLE = 10

# Detecting unused function arguments


def my_function2(arg1, arg2):
    """retuns both args, as a single tuple"""
    return arg1, arg2


# Identifying missing docstrings
def my_function3():
    """dummpy function"""


# Enforcing line length limit
LONG_LINE = (
    "This is a very long line that exceeds the line length limit defined by Pylint"
)

# Identifying unused class methods


class MyClass:
    """MyClass"""

    def unused_method(self):
        """unused_method"""

    def unused_method2(self):
        """unused_method2"""


# Detecting unreachable code
def my_function4():
    """returns a constant 10"""
    return 10
    # print("This code is unreachable")


# Identifying missing return statements in functions/methods


def my_function5():
    """.."""


# Enforcing consistent whitespace usage
INVALID_WHITESPACE = 10 + 5

# Identifying incorrect use of mutable default function arguments


def my_function6(arg=None):
    """function to demo antipattern"""
    if arg is None:
        arg = []
    arg.append(10)


# Checking for inconsistent use of quotation marks
INVALID_STRING = "This string uses single quotes instead of double quotes"

# Detecting unnecessary pass statements
try:
    1 / 0
except ZeroDivisionError:
    print("Dont divide by zero")


# Identifying incorrect variable reassignment
VARIABLE = 10
VARIABLE = "updated value"

"""
pylint can only list the problems, but not rectify themStop.

autopep8 can help to auto format


python b1_unformatted.py
python -m autopep8 b1_unformatted.py
python -m autopep8 -d b1_unformatted.py

cp b1_unformatted.py b0_unformatted.py.bak
python -m autopep8 -i b1_unformatted.py


TO update changes on same file
    autopep8 --in-place --aggressive --aggressive <filename>

To create backup and to changes
    cp b1_unformatted.py b1_unformatted.py.bak && autopep8 --aggressive --in-place b2_formatted.py


"""
