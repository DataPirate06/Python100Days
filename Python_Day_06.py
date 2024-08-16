#Variables and Data Types
from typing import Dict

a = 47612
print(a)
harry = 9
b = harry
print(b)

c = "Mohit"
print("The type of a is:", type(a))

d = complex(8 + 2)
e = complex(8, 2)
print(d)
print(e)

#lists are mutable
list1 = [8, 2, 3, [-4, 5], ["apple", "banana"]]
print(list1)

#Tuples are immutable(they cannot be changed or modified)
tuple1 = (("parrot", "sparrow"), ("lion", "tiger"))
print(tuple1)

#Dictionary is a collection of key-value pairs
Dict1 = {"name": "Mohit", "age": "20", "canVote": True}
print(Dict1)
