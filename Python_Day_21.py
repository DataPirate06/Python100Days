'''Day 21 of #100DaysOfCode. Today in this video, I learned about four types of function arguments in Python: default, keyword, required, and variable-length arguments. Default arguments have preset values, while keyword arguments allow specifying values using key-value pairs. Required arguments need correct positional order, and variable-length arguments accommodate extra arguments. Additionally, the return statement is used to pass values from functions back to the calling function.'''
# def average(a, b, c=1):
#   print("The average is ", (a + b + c) / 2)


def average(*numbers):
  # print(type(numbers))
  sum = 0
  for i in numbers:
    sum = sum + i
  # print("Average is: ", sum / len(numbers))
  # return 7
  return sum / len(numbers)


# Even if we give 2 return statements it takes the first one

# average(4, 6)
# average(b=9)

c = average(5, 6, 7, 1)
print(c)

# def name(**name):
#   # print(type(name))
#   print("Hello,", name["fname"], name["mname"], name["lname"])

# name(mname="Buchanan", lname="Barnes", fname="James")
