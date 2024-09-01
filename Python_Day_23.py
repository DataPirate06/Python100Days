#List Methods
'''Day 23 of #100DaysOfCode. Today in this video, I learned about various list methods in Python, including sort(), reverse(), index(), count(), copy(), append(), insert(), and extend(). These methods help in sorting lists, reversing their order, finding the index or count of an item, creating a copy of the list, appending items, inserting items at specific indexes, and extending a list with another collection datatype. Additionally, I learned that we can concatenate two lists to join them together. These methods make list manipulation in Python more efficient and convenient.'''
l = [11, 45, 1, 2, 4, 6, 1, 1]
print(l)
# l.append(7)
#l.sort()....ascending order
# l.sort(reverse=True).... It will sort the list in descending order
# l.reverse()
# print(l.index(1))
# print(l.count(1))
# m = l.copy()....If m=l then it will change the value of l but by doing copy it will not change the value of l
# m[0] = 0
# l.insert(1, 899)
m = [900, 1000, 1100]
k = l + m  #If we want to add two list then we can use this method
# print(k)
# l.extend(m)
print(l)
