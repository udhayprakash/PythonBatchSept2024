"""
Purpose: Dunder( Double underscore) Methods

"""

num1 = 100

print(num1 + 22)
print(num1.__add__(22))

assert num1 + 22 == num1.__add__(22)
print()


class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __add__(self, other):
        # print('additing')
        return Person(self.name, other.surname)

    def __str__(self):
        # return 'hello'
        return f"{self.name}_{self.surname}"

    # def __repr__(self):
    #     return 'hello'
    __repr__ = __str__
    
bhargav = Person("Bhargav", "sadhana")
print(bhargav)

father = Person("FatherName", "FatherSurname")
print(father)

mother = Person("MotherName", "MotherSurname")
print(mother)                       # __str__
print()

print(f'{mother + father        =}') # __repr__
print(f'{mother.__add__(father) =}')
