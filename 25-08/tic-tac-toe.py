import random

print("Welcome to Tic-Tac-Toe!")

def board_design():
  print(f"{board[0]}|{board[1]}|{board[2]}")
  print("---+---+---")
  print(f"{board[3]}|{board[4]}|{board[5]}")
  print("---+---+---")
  print(f"{board[6]}|{board[7]}|{board[8]}")

board = ["   " for _ in range(9) for _ in range(9)]
board_coords=[[x,y] for x in range(3) for y in range(3)]
used_coords=[]

print("Here's the board:")
board_design()

def player_move(p1,p2,symbol):
  if [p1,p2] in used_coords:
    print("This position is already taken. Try again.")
    p1=int(input("Enter the row (0, 1, or 2): "))
    p2=int(input("Enter the column (0, 1, or 2): "))
    player_move(p1,p2,symbol)
  else:
    used_coords.append([p1,p2])
    board[p1*3+p2]=f" {symbol} "
    board_design()
    print("\n")
    if (board[0]==board[1]==board[2]!="   ") or (board[3]==board[4]==board[5]!="   ") or (board[6]==board[7]==board[8]!="   ") or (board[0]==board[3]==board[6]!="   ") or (board[1]==board[4]==board[7]!="   ") or (board[2]==board[5]==board[8]!="   ") or (board[0]==board[4]==board[8]!="   ") or (board[2]==board[4]==board[6]!="   "):
      check_winner(symbol)
      used_coords.extend(board_coords)
    return

def check_winner(symbol):
  print(f"Player {symbol} wins!")
  return
  
while(len(used_coords)<9):
  try:

    p1=int(input("Enter the row (0, 1, or 2): "))
    p2=int(input("Enter the column (0, 1, or 2): "))
    player_move(p1,p2,"X")
    if len(used_coords)==9:
      break
    point_a,point_b=random.choice(board_coords)
    while [point_a,point_b] in used_coords:
      point_a,point_b=random.choice(board_coords)
    print(f"Computer chose: {point_a}, {point_b}")
    player_move(point_a,point_b,"O")
    if len(used_coords)==9:
      break
  except:
    print("Invalid input. Please enter 0, 1, or 2.")
    continue