"""
__lt__  <
__gt__  >
__eq__  =
__ne__  !=
__le__  <=

eg: a < b python tries a.__lt__(b)  if it returns NotImplemented then
it uses reflection and tries for b > a it b.__gt__(a)

If there is no __gt__ method implemented then python swaps operands and perform lessthan

eg: a > b. If there is no __gt__ in a class then it search for b < a


"""
from math import sqrt


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f"Vector {self.x, self.y}"
    
    def __eq__(self, other):
        if isinstance(other, tuple):
            other = Vector(*other)
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        return NotImplemented
    
    def __lt__(self, other):
        if isinstance(other, tuple):
            other = Vector(*other)
        if isinstance(other, Vector):
            return abs(self) < abs(other)
        return NotImplemented
    
    def __abs__(self):
        return sqrt(self.x ** 2 + self.y ** 2)

    
v1 = Vector(12, 20)
v2 = Vector(12, 20)
v3 = Vector(3, 4)
print(v1 == (12, 20))

print((12, 20) == v1)
print(v3 < v1)
