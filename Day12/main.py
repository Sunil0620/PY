# Project: Number Guessing Game!
import random
import art

def playGame():
    print("Welcome to the Number Guessing Game! \nI'm thinking of number between 1 to 100")
    print(art.logo2) 
    guess = random.randint(1, 100)
    guess_num = 1

    while True:
        difficulty = input("Choose a difficulty , type 'Hard' 😎 or 'easy' 🥰: ").lower()
        if difficulty in ['hard', 'easy']:  
            attempts = 5 if difficulty == "hard" else 10
            break
        print("Invalid. 🚫")
    
    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number")
        try:
            guess_num = int(input("Make a Guess: "))
        except ValueError:
            print("invalid. 🚫")
            continue
        
        if guess_num == guess:
            print(f"You Got it! the answer was {guess}. 🎉")
            return True
        if guess_num < guess:
            print("Too low. \nGuess again.🙂")
        elif guess_num > guess:
            print("Too high. \nGuess again.🙂")
        
        attempts -= 1
        
        if attempts == 0:
            print(f"You run out of guesses 🤡. the answer was {guess}. 😢")
            return False

while True:
    playGame()
    if input("\nWant to play again? (y/n): 😃").lower() != 'y':
        break
print("Thanks for playing! 💞")
