"""
Purpose: __repr__
"""


class TheProblem:
    def __init__(self, items):
        self.items = list(items)

    def __repr__(self):
        items = self.items
        return f"{items}"

    # def __str__(self):
    #     return 'str is called'

    __str__ = __repr__


# NOTE: print will call __str__ if present, else __repr__


p1 = TheProblem(range(50))
print(p1)           # str is called
print(f'{p1 = }')   # repr is called

# -----------------------------------------
import reprlib


class Solution:
    def __init__(self, items):
        self.items = list(items)

    def __repr__(self):
        items = reprlib.repr(self.items)
        return f"{items}"


p2 = Solution(range(50))
print(p2)

# print(
#     f"{p1 =}"
# )


# --------------------------------------------
class Foo(object):
    def __str__(self):
        return "Testing"

    def __repr__(self):
        return "Programming"


print("{!s} {!r}".format(Foo(), Foo()))
print("{0!s} {0!r}".format(Foo()))