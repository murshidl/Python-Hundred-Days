import random

print("""  
.------.   .------.  
|A     |   |K     |  
|  ♠   |   |  ♥   |  
|     A|   |     K|  
`------'   `------'  

██████  ██       ▄▄▄       ▄▄▄▄   ██   ██      ██ █████  ██   ██ 
██   ██ ██      ██ ██    ██   ██ ██  ██       ██ ██  ██ ██  ██  
██████  ██     ███████   ██   ██ █████        ██ █████  █████   
██   ██ ██     ██   ██   ██   ██ ██  ██  ██   ██ ██     ██  ██  
██████  ██████ ██   ██    ▀▄▄▄▀  ██   ██  █████  ██     ██   ██ 
""")

# Create deck
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
ranks = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]

deck = []
for suit in suits:
    for rank in ranks:
        deck.append(f"{rank} of {suit}")
random.shuffle(deck)

# Deal cards
player_cards = [deck.pop(), deck.pop()]
dealer_cards = [deck.pop(), deck.pop()]

# Card values
values = {
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
    "7": 7, "8": 8, "9": 9, "10": 10,
    "J": 10, "Q": 10, "K": 10, "A": 11
}

# Function to calculate hand value
def handval(hand):
    total = 0
    ace_count = 0
    for card in hand:
        rank = card.split()[0]
        total += values[rank]
        if rank == "A":
            ace_count += 1

    while total > 21 and ace_count:
        total -= 10
        ace_count -= 1

    return total

# Show initial cards
print("Your cards:", player_cards)
print("Dealer shows:", dealer_cards[0])
print("Your total:", handval(player_cards))

# Player turn
while True:
    move = input("Do you want to Hit or Stand? (H/S): ").upper()
    if move == "H":
        player_cards.append(deck.pop())
        print("Your cards:", player_cards)
        print("Your total:", handval(player_cards))
        if handval(player_cards) > 21:
            print("You busted! Dealer wins.")
            exit()
    elif move == "S":
        break
    else:
        print("Please enter H or S.")

# Dealer turn
print("\nDealer's turn:")
print("Dealer's cards:", dealer_cards)
while handval(dealer_cards) < 17:
    dealer_cards.append(deck.pop())
    print("Dealer draws a card:", dealer_cards[-1])
    print("Dealer's total:", handval(dealer_cards))

if handval(dealer_cards) > 21:
    print("Dealer busted! You win!")
    exit()

# Determine winner
player_total = handval(player_cards)
dealer_total = handval(dealer_cards)

print("\nFinal totals:")
print("Your total:", player_total)
print("Dealer total:", dealer_total)

if player_total > dealer_total:
    print("You win!")
elif player_total < dealer_total:
    print("Dealer wins!")
else:
    print("It's a tie!")
