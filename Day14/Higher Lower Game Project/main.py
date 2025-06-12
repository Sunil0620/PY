# Project
import random
from art import logo,vs
from gameData import data
def play_game():
    print(logo)
    score = 0
    game_continue = True
    account_b = random.choice(data)
    def fromat_data(acc):
        acc_name = acc["name"]
        acc_country = acc["country"]
        acc_descr = acc["description"]
        return f"{acc_name}, a {acc_descr}, from {acc_country}"
    def check_answer(guess, follower_a, follower_b):  
        if follower_a > follower_b:
            return guess == "a"
        
        return guess == "b"
    while game_continue:
        # if score > 0:
        #     print(f"You're right! Current score: {score}.")
        account_a = account_b
        account_b = random.choice(data)
        if account_a == account_b:
            account_b = random.choice(data)
            
        follower_count_a = account_a["follower_count"]
        follower_count_b = account_b["follower_count"]  
        print(f"Compare A: {fromat_data(acc = account_a)}.{follower_count_a}")
        print(vs)
        print(f"Against B: {fromat_data(acc = account_b)}.{follower_count_b}")
        answer = input("Who has more follower? Type 'A' or 'B': ").lower()
        print("\n" * 30)
        print(logo)
        
        is_correct = check_answer(answer,follower_count_a,follower_count_b)
        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            game_continue = False
    play_again = input("\nDo you want to play again? Type 'y' or 'n': ").lower()

    if play_again == 'y':
        print("\n" * 20)
        play_game()
    elif play_again == 'n':
        print("Thanks for playing!")
play_game()