import random
Rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
print("Welcome to Rock, Paper, Scissors Game!")
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors."))
choices = [Rock, paper, scissors]
random_choice = random.randint(0, 2)
if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose!")
elif user_choice == 0:
    print(f"You chose:",choices[user_choice])
    print(f"Computer chose:{choices[random_choice]}")
    if random_choice == 0:
        print("It's a draw!")
    elif random_choice == 1:
        print("You lose!")
    else:
        print("You win!")  
elif user_choice == 1:
    print(f"You chose:",choices[user_choice])
    print(f"Computer chose:{choices[random_choice]}")
    if random_choice == 0:
        print("You win!")
    elif random_choice == 1:
        print("It's a draw!")
    else:
        print("You lose!")
elif user_choice == 2:
    print(f"You chose:",choices[user_choice])
    print(f"Computer chose:",choices[random_choice])
    if random_choice == 0:
        print("You lose!")
    elif random_choice == 1:
        print("You win!")
    else:
        print("It's a draw!")
        