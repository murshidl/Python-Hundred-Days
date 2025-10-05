print("    ________\n"
"   |        |\n"
"   |  ====  |\n"
"   |________|\n"
"      ||||\n"
"      ||||\n"
"      ||||\n"
"     /____\\\n")

bids = {}

while True:
    name = input("Enter your name: ")
    price = int(input("Enter your bid: $"))
    bids[name] = price
    
    should_continue = input("Are there any other bidders? type 'yes' or 'no': ").lower()
    if should_continue == "no":
        break

print("Auction has ended.")

# Find winner
winner = max(bids, key=bids.get)
winning_bid = bids[winner]
print(f"The highest bid is: ${winning_bid}")
print(f"The winner is: {winner}")
print("All bids:", bids)
