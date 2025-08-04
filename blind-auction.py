print ("welcome to blind auction, the heighst bider will be the winner")
import os
def find_highest_bidder (bidding_dictionary) :
    winner = ""
    heighest_bid = 0
    for bidder in bidding_dictionary :
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > heighest_bid:
            heighest_bid = bid_amount
            winner = bidder
    print (---f"the winner is {winner} with a bid of ${heighest_bid}---")


bids = {}
continue_bidding = True

while continue_bidding :
    name = input("enter your name: ")
    price = int(input("enter your bid: $"))
    bids [name] = price

    should_continue = (input("is ther any other bidders?? Yes/No: ")).strip().lower()
    if should_continue == "no":
        continue_bidding = False
        os.system("clear")
        find_highest_bidder(bids)
    elif should_continue == "yes":
        os.system("clear")
       


