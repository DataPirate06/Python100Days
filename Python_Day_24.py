tup = (1, 2, 76, 342, 32, "green", True)
# tup[0] = 90
print(type(tup), tup)
print(len(tup))
tup1=(1) #this is not a tuple if u want to make a tuple of single element then u have to add a comma after the element like tup1=(1,).

print(type(tup1)) # this is not a tuple it is an integer 
print(tup[0])
print(tup[-1])
print(tup[2])
# print(tup[34])

if  3421 in tup:
  print("Yes 342 is present in this tuple")
tup2 = tup[1:4]
print(tup2)