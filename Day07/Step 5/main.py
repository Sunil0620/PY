# Hangman Game - Step 4
import random
#1 import the word list and stages from the respective files
from hangman_words import word_list 
from hangman_art import stages,logo
lives = 6

#3 print the logo
print(logo)
word = random.choice(word_list)
print(word)    
 
placeholder = ""
word_len = len(word)

for position in range(word_len):
    placeholder += "_"
print("word to guess:" + placeholder)

while "_" in placeholder:
#6:
    print(f"You have {lives} lives left")
    guess = input("Guess a letter: ").lower()
    display = ""
#4:  
    if guess in  placeholder:
        print("You've already guessed {guess}")
        continue
    
    for letter in range(word_len):
        if word[letter] == guess:
            display += guess
        else:
            display += placeholder[letter]
    placeholder = display   
    print(display)  
#5:    
    if guess not in word:
        lives -= 1
        print(f"{guess} is not in the word. You lose a life")
        print()
        if lives == 0:
            print(f"YOU LOSE \nThe word was {word}") 
            break

    if "_" not in placeholder:
        print("Congrats")
        if lives > 0:
            print("YOU WIN")
#2: import the stages and print the ASCII art
    print(stages[lives]) 