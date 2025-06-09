# Hangman Game - Step 2
import random
word_list = ["camel", "baboon", "banana" ]
word = random.choice(word_list)
print(word)  

#1 creating a placeholder for the word
placeholder = ""
word_len = len(word)
for position in range(word_len):
    placeholder += "_"
print(placeholder)
guess = input("Guess a letter: ").lower()

#2 create a display of underscores for each letter in the word
display = ""

for letter in word:
    if letter == guess:
        display += letter
    else:
        display += "_"
print(display) 

