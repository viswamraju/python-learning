"""
Any non zero number is true

An empty collection len(coll) == 0 is False

By default any custom object also has truth value
can override this by defining bool method
if bool is not defined checks for __len__ method

If there is no __bool__ method and __len__ method then it always returns True
"""

#
# class Person:
#     pass
#
#     def __len__(self):
#         return 0
#
#
# p1 = Person()
#
# if p1:
#     print('hey Hey')


class Person1:
    
    def __init__(self, length):
        self._length = length
        
    def __bool__(self):
        print("bool called")
        return self._length > 0
        
    def __len__(self):
        print("len called")
        return self._length
    

p1 = Person1(0)
p2 = Person1(1)

print(bool(p1))
print(bool(p2))

