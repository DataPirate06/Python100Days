#Enumerate function in python
#he enumerate function is a built-in function in Python that allows you to loop over a sequence (such as a list, tuple, or string) and get the index and value of each element in the sequence at the same time.

marks = [12, 56, 32, 98, 12,  45, 1, 4]

# index = 0
# for mark in marks:
#   print(mark)
#   if(index == 3):
#     print("Harry, awesome!")
#   index +=1

for index, mark in enumerate(marks, start=1):  # If we dont give start attribute it will by default take it from 0 enumerate(marks)
  print(mark)
  if(index == 3):
    print("Mohit, awesome!")
