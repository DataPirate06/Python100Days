#Methods in dictionary
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info)
info.update({'age':20})
info.update({'DOB':2001})
print(info)

info = {'name':'Karan', 'age':19, 'eligible':True}
info.clear()
print(info)

#The pop() method removes the key-value pair whose key is passed as a parameter.
info = {'name':'Karan', 'age':19, 'eligible':True}
info.pop('eligible')
print(info)

#The popitem() method removes the last key-value pair from the dictionary.
info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
info.popitem()
print(info)

