import os
from auction_art import logo
bids = {}
bidding = True
print(logo)
while bidding:
    print("Welcome to the secret Auction Program!")
    name = input("Enter your name: ")
    bid = int(input("What is your bid?: $"))
    bids = {name: bid}
    # or can be written as bids[name] = bid
    answer = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if answer == "yes":
        os.system("cls")
    else:
        bidding = False

highest_bid = 0
winner = ""
for names in bids:
    if bids[names] > highest_bid:
        highest_bid = bids[names]
        winner = names
    else:
        continue

print("The winner is {} with a bid of ${}.".format(winner, highest_bid))
