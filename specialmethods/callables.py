"""
Make any instance of an object callable by adding __call__ to class

Useful for creating function like objects that need to be maintain state
useful for creating decorator classes

"""

#
# class Person:
#     def __call__(self, *args, **kwargs):
#         print("__call__ called ..")
#
#
# p1 = Person()
# print('___________')
# p1()


# from functools import partial
# print(type(partial))
#
#
# def my_function(a, b, c):
#     return a, b, c
#
# print(type(my_function))
#
# partial_func = partial(my_function, 10, 20)
# print(partial_func(30))
# print(callable(partial_func))

from collections import defaultdict


class DefaultValue:
    def __init__(self):
        self.counter = 0
        
    def __call__(self, ):
        self.counter += 1
        return 'NA'
    
def1 = DefaultValue()
def2 = DefaultValue()
print(def1())
print(def1.counter)

    
