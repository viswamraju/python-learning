"""
__add__  +
__sub__  -
__mul__  *
__truediv__  /
__floordiv__  //
__mod__  %
__pow__  **


Eg:  a + b  python tries to call a.__add__(b)  The class of a should have implemented __add__(self, other) method
If this returns NotImplemented and operands are not of the same type
then python tries this b.__radd__(a)

Eg: 10 * v1 on calling this python tries to execute 10.__mul(v1). There is no multiplication on 10 with custom class
so it raises NotImplemented at the same time tries v1.__rmul__(10). even its not there then raises exception

__radd__, __rsub__, __rmul__

inplace operators

__iadd__    +=
__isub__    -=
__imul__    *=
__itruediv__   /=

__neg__   -a
__pos__   +a
__abs__   abs(a)

"""
from numbers import Real


class VectorDimensionMisMatch(TypeError):
    pass


class Vector:
    
    def __init__(self, *components):
        if len(components) < 0:
            raise ValueError('Cannot create an empty vector')
        for component in components:
            if not isinstance(component, Real):
                raise ValueError(f'Vector components must all be real numbers. {component} is invalid')
        self._components = components
    
    def __len__(self):
        return len(self._components)
    
    @property
    def components(self):
        return self._components
    
    @components.setter
    def components(self, *components):
        self._components = components
        
    def __repr__(self):
        return f"Vector {self.components}"
    
    def __add__(self, other):
        if not self.validate_type_and_dimension(other):
            return VectorDimensionMisMatch('vectors must be of same dimension')
        components = (x + y for x, y in zip(self.components, other.components))
        return Vector(* components)
        
    def __iadd__(self, other):
        return self + other
        
    def __sub__(self, other):
        if not self.validate_type_and_dimension(other):
            return NotImplemented
        components = (x - y for x, y in zip(self.components, other.components))
        return Vector(* components)
    
    def __mul__(self, other):
        if isinstance(other, Real):
            components = (x * other for x in self.components)
            return Vector(* components)
        if self.validate_type_and_dimension(other):
            components = (x * y for x, y in zip(self.components, other.components))
            return sum(components)
        return NotImplemented
            
    def __rmul__(self, other):
        print('rmul called')
        return self * other
    
    def validate_type_and_dimension(self, v):
        return isinstance(v, Vector) and len(v) == len(self)


# v1 = Vector(1, 2)
# v2 = Vector(20, 30, 40, 50)
#
# print(len(v1))
# print(len(v2))
#
# print(v1)
# print(v2)
# print(v1.components)
# v1.components = (1, 2, 3)
# print(v1.components)

# v1 = Vector(1, 2)
# v2 = Vector(10, 10)
# v3 = Vector(1, 2, 3)
#
# print(v1)
# print(v2)
#
# print(v1 + v2)
# print(v2 + v1)
# print(v1 + v3)

# v1 = Vector(1, 2)
# v2 = v1 * 10
# print(v2)
#
# print(10 * v1)

# v1 = Vector(1, 2)
# v2 = Vector(3, 4)
# print(v1 * v2)

v1 = Vector(10, 11)
print(id(v1))
v1 += Vector(10, 20)
print(id(v1))




