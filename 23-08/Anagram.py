import random

words=["python","kotlin","javascript","react","angular","node","express","laravel"]
score=0
flag=True

while flag:
  try:
    choice=input("Do you want to play(y/n):").lower()
    if(choice=='y'):
      string=random.choice(words)
      string_list=list(string)
      char_list=random.shuffle(string_list)
      shuffledCharacter="".join(string_list)
      print("Scrambled word:",shuffledCharacter)
      guess=input("Your guess:").lower()
      if(string==guess):
        print("Correct!")
        score+=1
      else:
        print("Incorrect, try again")
    elif(choice=='n'):
      print(f"Your total score is: {score}")
      print("Thank you!")
      flag=False
    else:
      print("Enter valid choice.")
  except:
    print("Something went wrong.")
