#Sets in python
'''
Sets do not maintain order i.e if u run a set it will print in any order 
sets do not store duplicate items
since sets are unordered we cannot access items using indexing
Sets are unchangeable, meaning you cannot change items of the set once created. 
'''

s = {2, 4, 2, 6}
print(s) #it will print {2,4,6} since there is '2' two times it will get printed only once

info = {"Carla", 19, False, 5.9, 19}
print(info) #it will print {False, 19, 5.9, 'Carla'} since there is '19' two times it and may change the order every time u run it since it is an unordered collection.

mohit = set() #this is how we can create an empty set if we try like mohit = {} then it will show an empty dictionary but not set.
print(type(mohit))

for value in info:
  print(value)