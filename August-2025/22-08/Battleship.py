import random

print("Welcome to Battleship")
print("The system has placed the battleship in a 5x5 grid")

def systemChoice():
  choose=lambda:[x for x in range(1,6)]
  systemRow=random.choice(choose())
  systemColumn=random.choice(choose())
  systemCoordinates=[systemRow,systemColumn]
  return systemCoordinates

def show():
  for i in range(5):
    for j in range(5):
      print(' * ',end='')
    print()

show()
coords=systemChoice()
# print(coords)
flag=True

while flag:
  try:
    userRow=int(input("Enter the row number (1-5): "))
    userColumn=int(input("Enter the column number (1-5): "))
    if(userRow not in range(1,6) or userColumn not in range(1,6)):
      print("Enter between 1 to 5")
      pass
    else:
      if(userRow==coords[0] and userColumn==coords[1]):
        print("Hit! You sunk ship.")
        flag=False
      else:
        print("Miss!")
  except:
    print("Invalid input. Please enter numeric values between 1 and 5.")