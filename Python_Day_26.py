#Exercice 2:Greetings
'''
Day 26 #100DaysOfCode. Today in this video 26, I learned how to create a Python program that greets me with "Good Morning," "Good Afternoon," or "Good Evening" based on the current hour. I used the time module and its strftime() function to obtain the current time in hours, minutes, and seconds. This exercise taught me the importance of tailoring program outputs to real-world conditions, and I gained valuable experience in using Python's built-in modules to access and manipulate time data.
'''

import time

t = time.strftime('%H:%M:%S')
hour = int(time.strftime('%H'))
# hour = int(input("Enter hour: "))
# print(hour)

if (hour >= 0 and hour < 12):
  print("Good Morning Sir!")
elif (hour >= 12 and hour < 17):
  print("Good Afternoon Sir!")
elif (hour >= 17 and hour < 24):
  print("Good Night Sir!")
