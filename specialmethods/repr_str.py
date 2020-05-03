"""
both used for creating a string representation of an object.

    typically __repr__ used by developers
    try to make it so that it can be used to recreate object
    otherwise make is as descriptive as possible
    called when using the repr function

    __str__ used by str(), or print() functions as well as formatting functions
    

if __str__ is not implemented python looks for __repr__.

If neither is implemented and since all objects inherit from “Object”, will use __repr__ defined there instead.
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __repr__(self):
        print("__repr__ called")
        return f"Person({self.name}, {self.age})"

    def __str__(self):
        print("__str__ called")
        return f"<Person: {self.name}>"
    

p1 = Person('viswam', 28)
p2 = Person('hari', 29)

print(repr(p1))
print(p1)
print(str(p1))
print(f"Person instance p1: {p1}")
