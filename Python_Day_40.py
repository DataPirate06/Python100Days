# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

# Your program should ask whether you want to code or decode

import random
import string

str=input("please enter the word to encode or decode: ")
reply=int(input("Enter 1 for Encoding / Enter 2 for Decoding / Enter 0 to quit "))
if(reply==1):
        if len(str)>=3:
            a=str[0]
            str=str[1:]
            str=str+a
            letters = string.ascii_lowercase
            result_start = ''.join((random.choice(letters)) for x in range(3))  
            result_end=''.join((random.choice(letters)) for x in range(3))
            print(result_start+str+result_end)
        else:
            print(str[::-1])

elif(reply==2):

        if len(str)<3:
            print(str[::-1])
        else:
            str=str[3:-3]
            a=str[-1]
            str=str[:-1]
            print(a+str)

if(reply==0):
     print("Exiting the program")