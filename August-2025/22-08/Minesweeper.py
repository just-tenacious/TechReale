import random

def land():
  for i in range(1,6):
    for j in range(1,6):
      print(' ? ',end='')
    print()

def mines():
  mineChoice=[]
  for i in range(1,6):
    for j in range(1,6):
      mineChoice.append([i,j])
  mines=random.sample(mineChoice,5)
  return mines

print("Welcome to Minesweeper!")

land()
mine=mines()
# print(mine)
flag=True

while flag:
  try:
    row=int(input("Enter row:"))
    col=int(input("Enter col:"))
    if(row not in range(1,6) or col not in range(1,6)):
      print("Enter between 1 to 5")
    else:
      if([row,col] in mine):
        print("Boom! Game Over.")
        flag=False
      else:
        print("Safe! Near:",end='')
        count=0
        for i in mine:
          if(((i[0])+1)==row or ((i[0])-1)==row or (i[1]+1)==col or ((i[1])-1)==col):
            count+=1
        print(count)
  except:
    print("Something went wrong!!")