print("Welcome to Word Ladder.")

words = ["cold", "cord", "word", "ward", "warm","card","corm","worm","worn","corn"]

start = "cold"
target = "warm"
current = start
steps = 0

print("Word Ladder:", start, "->", target)

while current != target:
    next_word = input("Enter next word: ").lower()
    if next_word in words:
      
      diff = 0
      for i in range(len(current)):
        if current[i] != next_word[i]:
          print("current:", current[i], "next_word:", next_word[i], "i:", i)
          diff += 1
      if diff != 1:
        print("Must change exactly one letter. Try again.")
        continue
      steps += 1
      current = next_word
    else:
      print("Not a valid word. Try again.")
      continue

print("You solved it in", steps, "steps!")
