# Hangman Game - Step 3
import random
word_list = ["camel", "baboon", "banana" ]
word = random.choice(word_list)
print(word)    

placeholder = ""
word_len = len(word)
for position in range(word_len):
    placeholder += "_"
print(placeholder)

#1 while loop to keep asking for a letter until the user guesses the word
while "_" in placeholder:
    guess = input("Guess a letter: ").lower()
    display = ""
    
#2 update the display with the guessed letter to keep previous guesses
    for letter in range(word_len):
        if word[letter] == guess:
            display += guess
        else:
            display += placeholder[letter]
    placeholder = display   
    print(display)  

    if "_" not in placeholder:
        print("Congrats") 