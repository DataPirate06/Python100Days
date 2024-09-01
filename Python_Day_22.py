#Introduction to Lists
marks = [3, 5, 6, "Mohit", True, 6, 7, 2, 32, 345, 23]
# print(marks)
# print(type(marks))
# print(marks[0])
# print(marks[1])
# print(marks[2])
# print(marks[3])
# print(marks[4])
# print(marks[5])

# print(marks[-3]) # Negative index
# print(marks[len(marks)-3]) # Positive index
# print(marks[5-3]) # Positive index
# print(marks[2]) # Positive index

# if "6" in marks:
#   print("Yes")
# else:
#   print("No")
'''Day 22 of #100DaysOfCode. Today in this video, I learned that Python lists are ordered collections of data items, storing multiple items in a single variable. Lists can contain various data types and are changeable. Items in a list have unique indexes, accessible via positive and negative indexing. We can also check if an item is in a list, specify index ranges, and use list comprehensions to create new lists from other iterables based on conditions.'''
# Same thing applies for strings as well!
# if "Mo" in "Mohit":
#   print("Yes")

# print(marks[0:7])
# print(marks[1:9])
# print(marks[1:9:3])

lst = [i * i for i in range(10)]
print(lst)
lst = [i * i for i in range(10) if i % 2 == 0]
print(lst)
