from art import logo
import os

os.system('cls')

print(logo)


bids = {}
bidding_finished = False

def find_highest_bidder(bidding_recoard):
    highest_bid = 0
    winner = ""
    for bidder in bidding_recoard:
        bid_amount = bids[name]
        if bid_amount>highest_bid:
            highest_bid = bid_amount
            winner = bidder

        print(f"The winner is {winner} with a bid  of ${highest_bid}")

while not bidding_finished:
    name = input("What is your name ? \n")
    price = int(input("What your bid ? \n$"))
    bids[name]= price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'. \n")
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bidding_recoard=bids)
    elif should_continue == "yes":
        os.system('cls')
        

print(bids)
