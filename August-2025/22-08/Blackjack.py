import random

print("Welcome to Blackjack!")

def sum(lst):
  card=['K','Q','J','A']
  if(lst[0] in card):
    lst[0]=10
  if(lst[1] in card):
      lst[1]=10
  return lst[0]+lst[1]

cards=[2,3,4,5,6,7,8,9,10,'K','Q','J','A']
# cards=[2,3,4,5,6,7,8,9,10]

userCards=list(random.sample(cards,3))
dealerCards=list(random.sample(cards,2))

# print(userCards)
# print(dealerCards)

preSum=sum(userCards)
postSumList=[preSum,userCards[2]]

print(f"Your cards: [ {userCards[0]} , {userCards[1]} ] -> Total: {preSum}")
print(f"Dealer cards: [ {dealerCards[0]} , ? ]")

choice=input("Hit or Stand:").lower()

if(choice=="hit" or choice=="stand"):
  if(choice=="hit"):
    print(f"You drew: {userCards[1]} -> Total: {sum(postSumList)}")

    print(f"Dealer reveals: [ {dealerCards[0]} , {dealerCards[1]} ] -> Total: {sum(dealerCards)}")

    if(sum(postSumList)>21 and sum(dealerCards)>21):
      if(sum(postSumList)>sum(dealerCards)):
        print("You win!!")
      elif(sum(postSumList)<sum(dealerCards)):
        print("Dealer wins!!")
      else:
        print("It's a draw!!")
    elif(sum(postSumList)<=21):
      print("You win!!")
    elif(sum(dealerCards)<=21):
      print("Dealer wins!!")
    else:
      print("It's a draw!!")
  
  else:
    print("Hope you enjoyed!!")
else:
  print("Invalid choice")