# Project: the Secret Auction Program Instructions 
import art
print(art.logo)


def find_highest_bidder(bidding_dict):
    highest_bid = 0
    winner = ""
    
    for bidder in bidding_dict:
        bid_amount = bidding_dict[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
            
    print(f"The winner is {winner} with a bid of ${highest_bid}.")
    
    
bids = {}
continue_bidding = True

while continue_bidding:
    
    name = input("what is your name?:")
    bid = int(input("What is your bid?: $"))
    bids[name] = bid
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder(bids)
    elif should_continue == "yes":
        print("\n" * 100)
        