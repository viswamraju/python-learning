class Person:
    __slots__ = ['name', '_age']
    
    def __init__(self, name):
        self.name = name
        self._age = None
    
    @property
    def age(self, ):
        return self._age
    
    @age.setter
    def age(self, value):
        self._age = value
        
    def __str__(self):
        return f"<Person: name={self.name}, age={self._age}>"
    

p = Person('viswam')
setattr(p, 'age', 28)
setattr(p, 'dept', 'ece')
print(p)
