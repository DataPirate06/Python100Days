# f-string in python
letter = "Hey my name is {1} and I am from {0}"
country = "India"
name = "Mohit"

print(letter.format(country, name)) #old method...String formatting can also be done by this method
print(f"Hey my name is {name} and I am from {country}")
print(f"We use f-strings like this: Hey my name is {{name}} and I am from {{country}}") #if we want to print it as it is
price = 49.09999
txt = f"For only {price:.2f} dollars!" #:.2f is used to print only 2 decimal places
print(txt)
# print(txt.format())
print(type(f"{2 * 30}"))