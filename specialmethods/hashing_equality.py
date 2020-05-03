"""
An object to be usable in a mapping type
must be hashable

Key in a dictionary must be hashable. implement __hash__. should also implements __eq__ metyhod

if __eq__ is implemented __hash__ is implicitly sets to None unless hash is implemented.

By default when __hash__ override is not specified __hash__ used id of object.
                __eq__ uses identity ie. is eg: a is b

print(dir(object))

After adding __eq__ method object becomes unhashable unless you implement hash explicitly
If we dont implement hash then we cannot use them as keys in dictionary

By default with out overriding __eq__. Two objects becomes equal if they have same id. same memory location.

To add objects as keys in dictionary then objects hash and __eq__ should
be true then only it overrides existing key

If two objects hash is same and __eq__ is also same then adding these two objects as keys to dictionary gives only
one key.

If two objects hash is different and __eq__ is  same then adding these two objects as keys to dictionary gives two
 keys.  Thats why Its always better to override __eq__ and hash methods and the variables we are using for equality
 and hash should be immutable (should not able to change) to avoid any issues

"""

#
# class Person:
#     pass
#
#
# p1 = Person()
# p2 = Person()
# print(hash(p1), hash(p2))

# print(p1 == p2)

import random


class Person:
    def __init__(self, name):
        self._name = name
    
    @property
    def name(self):
        return self._name
        
    def __eq__(self, other):
        return isinstance(other, Person) and self.name == other.name
    
    def __repr__(self):
        return f"Person(name= {self.name})"
    
    def __hash__(self):
        return 123


p1 = Person("viswam")
p2 = Person("viswam")
print(p1.__hash__(), p2.__hash__())
a = dict()
a[p1] = 'viswamraj'
a[p2] = 'viswamraj1'
print(a)







