#Picking a Random Words and Checking Answers 
import random
word_list = ["camel", "baboon", "banana" ]
#1 choosing a random word
word = random.choice(word_list)
print(word)  
#2 Guessing a letter
guess = input("Guess a letter: ").lower()
print(guess)
#3 Checking if the letter is in the word
for letter in word:
    if letter == guess:
        print("Right!")
    else:
        print("Wrong!")
