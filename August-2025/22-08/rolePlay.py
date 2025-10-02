import random as r

playerCombat={"HP":100,"Attack":30,"Defense":20,"Level":1}
enemyList={1:{"Name":"Goblin","HP":50,"Attack":15,"Defense":5,},2:{"Name":"Orc","HP":35,"Attack":25,"Defense":10},3:{"Name":"Dragon","HP":60,"Attack":40,"Defense":20}}

print("Welcome to Python RPG!")
player=input("Enter your hero name: ")

print(f"Hello {player}, prepare for battle!")

enemyChoice=r.choice(list(enemyList.keys()))

print(f"Your enemy {enemyList[enemyChoice]["Name"]} appears!")
print (f"Your HP: {playerCombat['HP']} | Enemy HP: {enemyList[enemyChoice]['HP']}")

action=int(input("Choose your action: 1. Attack  2. Defend  3. Run"))