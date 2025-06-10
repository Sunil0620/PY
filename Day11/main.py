# Project : Blackjack / 21
import random
import art


def deal_cards():
    """Returns a random card from the deck."""
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]  # J, Q, K are represented as 10 and A as 11
    return random.choice(cards)

def calculate_score(cards):
    """Calculates the score of the given cards."""
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # Blackjack 
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)  # Convert Ace from 11 to 1
    return sum(cards)

def compare(u_score, c_score):
    """Compares player and computer scores to determine the winner."""
    if u_score == c_score:
        return "Draw "
    elif c_score == 0:
        return "Lose, opponent has blackjack 😱"
    elif u_score == 0:
        return "You win with a blackjack 😎"
    elif u_score > 21:
        return "You went over. You lose 😭"
    elif c_score > 21:
        return "Opponent went over. You win 😁"
    elif u_score > c_score:
        return "You win 😃"
    else:
        return "You lose 😤"
       
def play_Game():
    print(art.logo)
    user_cards = []
    computer_cards = []
    isGameOver = False

    for _ in range(2):
        user_cards.append(deal_cards())
        computer_cards.append(deal_cards())
        
    while not isGameOver:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards) 
        print(f"Your Cards: {user_cards}, Current Score: {user_score}")
        print(f"Computer First Card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            isGameOver = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_cards())
            else: 
                isGameOver = True
            
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_cards())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")  
    print(compare(user_score,computer_score))

while True:
    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n':").lower()
    if play == "y":
        print("\n" * 20)
        play_Game()
    else:
        break
