#String sclicing 
names="Mohit,Sharad"
print(names[0:6])
print(len(names))

fruit = "Mango"
mangoLen = len(fruit)
print(mangoLen)
# print(fruit[0:4]) # including 0 but not 4
# print(fruit[1:4]) # including 1 but not 4
# print(fruit[:5])
# print(fruit[0:-3])
# print(fruit[:len(fruit)-3])
print(fruit[-1:len(fruit) - 3])
print(fruit[-3:-1]) #It will calculate as [len(fruit)-3:len(fruit)-1] i.e. [2:4]

nm="Mohit"
print(nm[-4:-2])
