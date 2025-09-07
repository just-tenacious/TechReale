
print("Welcome to Sudoku Game!")

board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Display board
def print_board(b):
    for i in range(9):
      for j in range(9):
        if b[i][j] == 0:
          print("_", end=" ")
        else:
          print(b[i][j], end=" ")
        if (j+1) % 3 == 0 and j < 8:
          print("|", end=" ")
      print()
      if (i+1) % 3 == 0 and i < 8:
        print("-"*21)

# Check if placing num is valid
def is_valid(b, row, col, num):
  if num in b[row]:
    return False
  for i in range(9):
    if b[i][col] == num:
      return False

  start_row, start_col = (row//3)*3, (col//3)*3
  for i in range(start_row, start_row+3):
    for j in range(start_col, start_col+3):
      if b[i][j] == num:
        return False
    return True

print("Welcome to Sudoku!")
print_board(board)

while True:
  try:
    row, col, num = map(int, input("Enter row, col, number (1-9): ").split())
    row -= 1
    col -= 1

    if board[row][col] != 0:
      print("Cell already filled! Try another.")
      continue
    if is_valid(board, row, col, num):
      board[row][col] = num
      print(f"Placed {num} at ({row+1},{col+1})!")
    else:
      print("Invalid move! Try again.")
    print_board(board)

  except:
    print("Please enter row col number properly (e.g., 1 3 4).")
