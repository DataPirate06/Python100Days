#String methods
# Strings are immutable
a = "!!!Mohit!!!!!!!!!!!"
print(len(a))
print(a)
print(a.upper())  #Creates a new string
print(a.lower())
print(a.rstrip(
    "!"))  #Removes the trailing characters does not remove leading characters
b = "!!!Mohit!! !!!!!!!!! Mohit"
print(b.replace("Mohit", "John"))
print(b.split(" "))  #Splits the string at the whitespace and create a list
blogHeading = "introduction tO jS"
print(blogHeading.capitalize()
      )  #Capitalizes the first letter of the string and lowercases the rest

str1 = "Welcome to the Console!!!"
print(str1.endswith("!!!"))  #Checks if the string ends with the given value

print(str1.endswith(
    "to", 4,
    10))  #Checks if the string ends with the given value in the given range

print(str1.find(
    "to"))  #Finds the first occurence of the given value and returns its index
print(str1.find("ot"))  #If the value is not found, it returns -1

print(str1.index("to"))
print(str1.isalpha())  #Returns true if the string is only made up of alphabets

print(str1.isalnum()
      )  #Returns true if the string is made up of alphabets and numbers

print(str1.islower()
      )  #Returns true if the string is made up of lower case alphabets
print(str1.isupper()
      )  #Returns true if the string is made up of upper case alphabets
print(str1.isprintable())  #Returns true if the string is printable

str2 = "Welcome\n"
print(str2.isprintable())  #\n is not a printable

str1 = "         "  #using Spacebar
print(str1.isspace())
str2 = "  "  #using Tab
print(str2.isspace())

str1 = "World Health Organization"
print(
    str1.istitle()
)  #Returns true if the string is a title,it returns true only if the first letter of each word is capatilazed

str2 = "To kill a Mocking bird"
print(str2.istitle())

str1 = "Python is a Interpreted Language"
print(str1.startswith(
    "Python"))  #Returns true if the string starts with the given value

str1 = "Python is a Interpreted Language"
print(
    str1.swapcase()
)  #Swaps the case of the string,converts lowercase to uppercase and vice-versa

str1 = "His name is Dan. Dan is an honest man."
print(str1.title())  #Capitalizes the first letter of each word
