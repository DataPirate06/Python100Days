#KBC program
sum=0;
print("Welcome to KBC")
print("Let's start the game")
questions=[["What is the capital of India?","Delhi"],["What is the capital of Uttar Pradesh?","Lucknow"],["What is the capital of Maharashtra?","Mumbai"]]

for i in range(0,len(questions)):
  print(questions[i][0])
  ans=input("Enter your answer: ")
  if(ans==questions[i][1]):
    print("Correct Answer")
    sum=sum+1000
  else:
    print("Wrong Answer")
    break
print("You won ",sum," rupees")
  