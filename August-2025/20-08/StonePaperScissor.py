import random as r

def result(user,system):
  print(f"user:{user} and system:{system}")
  if(user==system):
    print("Match is draw")
    return -1
  else:
    if(system=='stone' or (system=='scissors' and user=='paper')):
      print("System Won")
      return 0
    else:
      print("User Won")
      return 1

systemChoiceList=["stone","paper","scissors"]
flag=True

while(flag):
  try:
    print("***********MENU******************")
    print("1. Stone")
    print("2. Paper")
    print("3. Scissors")
    print("4. EXIT")
    userChoice=int(input("\nEnter your choice:"))
    systemChoice=r.choice(systemChoiceList)
    if(userChoice==1):
      userChoice='stone'
      result(userChoice,systemChoice)
    elif(userChoice==2):
      userChoice='paper'
      result(userChoice,systemChoice)
    elif(userChoice==3):
      userChoice='scissors'
      result(userChoice,systemChoice)
    elif(userChoice==4):
      print("Thank you..")
      flag=False
    else:
      print("Please enter valid choice..")
  except:
    print("Please enter a valid input.")