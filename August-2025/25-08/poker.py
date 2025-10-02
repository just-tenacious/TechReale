import random

print("Welcome to Poker")

poker_deck = [
    ["A♠", "2♠", "3♠", "4♠", "5♠", "6♠", "7♠", "8♠", "9♠", "10♠", "J♠", "Q♠", "K♠"],  
    ["A♥", "2♥", "3♥", "4♥", "5♥", "6♥", "7♥", "8♥", "9♥", "10♥", "J♥", "Q♥", "K♥"],  
    ["A♣", "2♣", "3♣", "4♣", "5♣", "6♣", "7♣", "8♣", "9♣", "10♣", "J♣", "Q♣", "K♣"],  
    ["A♦", "2♦", "3♦", "4♦", "5♦", "6♦", "7♦", "8♦", "9♦", "10♦", "J♦", "Q♦", "K♦"]  
]

card_values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

def deal_hand(deck, hand_size=5):
  hand = []
  while len(hand) < hand_size:
    suit = random.choice(deck)
    card = random.choice(suit)
    if card not in hand:
      hand.append(card)
  return hand

def get_card_rank(card):
  return card[:-1]

user = deal_hand(poker_deck)
print("Your hand: ", user)

dealer = deal_hand(poker_deck)
print("Dealer's hand: ", dealer)

userValues = {}
for card in user:
  rank = get_card_rank(card)
  if rank in userValues:
    userValues[rank]+=1
  else:
    userValues[rank]=1

dealerValues = {}
for card in dealer:
  rank = get_card_rank(card)
  if rank in dealerValues:
    dealerValues[rank]+=1
  else:
    dealerValues[rank]=1

# print("User's unique card ranks:", userValues)
# print("Dealer's card counts:", dealerValues)

def evaluate_hand(values):
  counts = sorted(values.values(), reverse=True)
  if counts == [4, 1]:
    return (1,"Four of a Kind")
  elif counts == [3, 2]:
    return (2,"Full House")
  elif counts == [3, 1, 1]:
    return (3,"Three of a Kind")
  elif counts == [2, 2, 1]:
    return (4,"Two Pair")
  elif counts == [2, 1, 1, 1]:
    return (5,"One Pair")
  else:
    return (6,"High Card")
  
user_rank,user_hand_rank = evaluate_hand(userValues)
dealer_rank,dealer_hand_rank = evaluate_hand(dealerValues)

print("User's best hand:", user_hand_rank)
print("Dealer's best hand :", dealer_hand_rank)

if(user_rank<dealer_rank):
  print("Congratulations! You won.")
elif(dealer_rank<user_rank):
  print("Dealer won.")
else:
  print("It's a tie!")