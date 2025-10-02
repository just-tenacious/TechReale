import random as r

choice=int((r.random())*100)
result=list()
# print(choice)
counter=0

while(counter<3):
  try:
    userInput=int(input("\nGuess the number:"))
    counter+=1
    if(choice==userInput):
      print("Congratulations! You guessed it right.")
      break
    else:
      if(choice<=50):
        result.append("The number is less than or equal to 50")
        if(choice in range(0,26)):
          result.append("The number in between 0 to 25")
          if(choice in range(0,14)):
            result.append("The number is between 0 to 13")
          else:
            result.append("The number is in between 14 to 25")
        if(choice in range(25,51)):
          result.append("The number in between 25 to 50")
          if(choice in range(25,39)):
            result.append("The number is between 25 to 38")
          else:
            result.append("The number is in between 39 to 50")
      else:
        result.append("The number is more than 50")
        if(choice in range(50,76)):
          result.append("The number in between 50 to 75")
          if(choice in range(51,76)):
            result.append("The number is between 51 to 75")
          else:
            result.append("The number is in between 76 to 99")
        if(choice in range(75,100)):
          result.append("The number in between 75 to 100")
      if(counter==1):
        print(result[0])
      elif(counter==2):
        print(result[1])
      elif(choice==3):
        print(result[2])
      else:
        print(f"The number was {choice}")      
  except:
    print("Please enter a valid number.") 