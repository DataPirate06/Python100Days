# dic strings
'''Day 29 of #100DaysOfCode. Today in this video, I delved into Python docstrings, which are string literals that follow the definition of a function, method, class, or module. They serve as documentation for our code and can be accessed using the '__doc__' attribute. I also explored the differences between Python comments and docstrings. Furthermore, I learned about PEP 8, a guide for Python coding style, and The Zen of Python, which outlines the guiding principles for Python's design.PEP stands for Python Enhancement Proposal'''

def square(n):
  '''Takes in a number n, returns the square of n'''
  print(n**2)
square(5)
print(square.__doc__) #docstrings are not ignored by python interpreter they are different from comments, they are executed only when we use them just below the function name.

def cube(n):
  print(n)
  '''Takes in a number n, returns the square of n'''
  print(n**3)
cube(5)
print(square.__doc__)