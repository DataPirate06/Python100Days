#i = int(input("Enter the number: "))
#print(i)
#while(i<=38):
  #i = int(input("Enter the number: "))
  #print(i)

#print("Done with the loop")

# count = 5
# while (count > 0):
#   print(count)
#   count = count - 1
# else:
#   print("I am inside else")


#There is no such syntax for do while loop in python 
# do {
  # loop body;
# }while(condition);

secret_word = "python"
counter = 0

while True:
    word = input("Enter the secret word: ").lower()
    counter = counter + 1
    if word == secret_word:
        break
    if word != secret_word and counter > 7: 
        break