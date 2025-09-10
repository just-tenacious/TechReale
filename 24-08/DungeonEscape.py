import random

print("Welcome to Dungeon Escape!")

dungeon=[["_"] * 5 for _ in range(5)]
dungeon[0][0] = "E"

print("Dungeon Layout:")
for row in dungeon:
  print(" ".join(row))

player_pos = [0, 0]

exit_point=[random.randint(0, 4), random.randint(0, 4)]

while True:
  exit_point=[random.randint(0, 4), random.randint(0, 4)]
  if exit_point != player_pos:
    break

traps=[]
while len(traps) < 3:
  trap=[random.randint(0, 4), random.randint(0, 4)]
  if trap != player_pos and trap != exit_point and trap not in traps:
    traps.append(trap)

treasures=[]
while len(treasures) < 3:
  treasure=[random.randint(0, 4), random.randint(0, 4)]
  if treasure != player_pos and treasure != exit_point and treasure not in traps and treasure not in treasures:
    treasures.append(treasure)

# print(traps)
# print(treasures)
# print(exit_point)

player_row,player_col=0,0
hp=100
score=0

while True:
  print(f"\nHP: {hp} | Score: {score}")
  print("Options: (N)orth, (S)outh, (E)ast, (W)est")
  move = input("Move: ").strip().upper()

  if move == "N":
    new_row, new_col = player_row - 1, player_col
  elif move == "S":
    new_row, new_col = player_row + 1, player_col
  elif move == "E":
    new_row, new_col = player_row, player_col + 1
  elif move == "W":
    new_row, new_col = player_row, player_col - 1
  else:
    print("Invalid move. Use N/S/E/W.")
    continue

  if not (0 <= new_row < 5 and 0 <= new_col < 5):
    print("You hit a wall!")
    continue
  player_row, player_col = new_row, new_col
  cell = dungeon[player_row][player_col]

  if cell == "_":
    print("You walk through a dark corridor...")
  elif cell == "T":
    hp -= 20
    print("Oh no! You stepped on a trap. HP -20.")
    dungeon[player_row][player_col] = "_"
  elif cell == "X":
    score += 10
    print("You found a treasure chest! Score +10.")
    dungeon[player_row][player_col] = "_"
  elif cell == "E":
    print("You escaped the dungeon with", hp, "HP and", score, "score!")
    break
  if hp <= 0:
    print("You died in the dungeon!")
    break