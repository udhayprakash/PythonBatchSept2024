"""
Purpose: Python is a dynamic Typed Language.
    Progamming Languages
        - Classficiation
            1. Static-Typed Languages
                - first declare the variables, &
                - then use them
                    int a, float b  # Declaration
                    a = 10          # initialization

            2. Dynamic Typed Languages (Python, perl, ruby)
                 - create when you need. No declaration needed
                    num1 = 123

data types in python - int, float, complex, bool, None
"""
num1 = 100

print(num1)
type(num1)

print(type(num1))

print('num1 =', num1)
print("num1 =", num1)


print("num1 =", num1, "type(num1) =", type(num1))

# Python is a dynamic-typed language
num1 = 200
print("num1 =", num1, "type(num1) =", type(num1))

num1 = 200.
print("num1 =", num1, "type(num1) =", type(num1))

num1 = 200.0
print("num1 =", num1, "type(num1) =", type(num1))

num1 = 200.0,
print("num1 =", num1, "type(num1) =", type(num1))
print()


num1 = .200
print("num1 =", num1, "type(num1) =", type(num1))

num1 = .200j
print("num1 =", num1, "type(num1) =", type(num1))

num1 = 10 + .200j
print("num1 =", num1, "type(num1) =", type(num1))
print()


num1 = "10 + .200j"
print("num1 =", num1, "type(num1) =", type(num1))

num1 = "3"
print("num1 =", num1, "type(num1) =", type(num1))

num1 = "three"
print("num1 =", num1, "type(num1) =", type(num1))
print()

num1 = True
print("num1 =", num1, "type(num1) =", type(num1))

num1 = False
print("num1 =", num1, "type(num1) =", type(num1))

# num1 = true
# print("num1 =", num1, "type(num1) =", type(num1))
# NameError: name 'true' is not defined. Did you mean: 'True'?

num1 = "true"
print("num1 =", num1, "type(num1) =", type(num1))
print()


num1 = None
print("num1 =", num1, "type(num1) =", type(num1))

num1 = "None"
print("num1 =", num1, "type(num1) =", type(num1))

# NOTE: Strings need to be declared in quotes