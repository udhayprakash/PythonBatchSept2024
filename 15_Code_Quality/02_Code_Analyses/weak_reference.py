import weakref

print(dir(weakref))

"""


In [5]: [attr for attr in dir(list) if 'weakref' in attr]
Out[5]: []

In [6]: [attr for attr in dir(int) if 'weakref' in attr]
Out[6]: []

In [7]: [attr for attr in dir(float) if 'weakref' in attr]
Out[7]: []

In [8]: [attr for attr in dir(None) if 'weakref' in attr]
Out[8]: []

In [9]: [attr for attr in dir(str) if 'weakref' in attr]
Out[9]: []

In [10]: [attr for attr in dir(list) if 'weakref' in attr]
Out[10]: []

In [11]: [attr for attr in dir(tuple) if 'weakref' in attr]
Out[11]: []

In [12]: [attr for attr in dir(set) if 'weakref' in attr]
Out[12]: []

In [13]: [attr for attr in dir(dict) if 'weakref' in attr]
Out[13]: []

In [14]: class MyClass:
    ...:     pass
    ...: 

In [15]: [attr for attr in dir(MyClass) if 'weakref' in attr]
Out[15]: ['__weakref__']

In [16]: inst1 = MyClass()

In [17]: [attr for attr in dir(inst1) if 'weakref' in attr]
Out[17]: ['__weakref__']
"""

class A:
    pass


a = A()
b = weakref.ref(a)
c = weakref.ref(a)

print(f"{id(a) =}")
print(f"{id(b) =}")
print(f"{id(c) =}")


assert b is c
assert b is a.__weakref__
print(weakref.getweakrefs(a))



a.ANIMAL = 'DONKEY'
print(f'{a.ANIMAL =}')

# print(f'{b.ANIMAL =}')
# AttributeError: 'weakref.ReferenceType' object has no attribute 'ANIMAL'

# print(f'{c.ANIMAL =}')


b.COLOR = 'RED'
print(f'{b.COLOR =}')