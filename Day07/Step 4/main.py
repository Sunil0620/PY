# Hangman Game - Step 4
import random
stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\ |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', r'''
  +---+
  |   |
      |
      |
      |
      |
========='''
]   

word_list = ["camel", "baboon", "banana" ]
#1 Initialize the number of lives
lives = 6
word = random.choice(word_list)
print(word)    

placeholder = ""
word_len = len(word)
for position in range(word_len):
    placeholder += "_"
print(placeholder)

while "_" in placeholder:
    guess = input("Guess a letter: ").lower()
    display = ""
    
    for letter in range(word_len):
        if word[letter] == guess:
            display += guess
        else:
            display += placeholder[letter]
    placeholder = display   
    print(display)  
    
#2 
    if guess not in word:
        lives -= 1
        print("you lose a life")
        if lives == 0:
            print("YOU LOSE")
            break

    if "_" not in placeholder:
        print("Congrats")
        if lives > 0:
            print("YOU WIN")

#3 Print the ASCII art
    print(stages[lives])