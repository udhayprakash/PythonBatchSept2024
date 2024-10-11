# globals(), locals()
from pprint import pp


pi = 3.1415
mydict = {'a': 'apple'}

def myfunc():
    pi_local = 6.21321
    mydict_local = {'b': 'ball'}

    print(f'\ninside  - {locals()  =}')
    print(f'inside  - ')
    pp(globals())
    assert globals() != locals()

myfunc()

print()

assert locals() == globals()



import sys

print(sys.getrecursionlimit()) # 1000 -- in script mode ; 3000 in interactive mode