#Treasure Island Game
#Multi-line print statement

print(r'''**********************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____/__
*******************************************************************************
''')
#Multiple if statements

print("  Welcome to Treasure Island. \nYour mission is to find the treasure.")
path = input("Your are at a crossroad where do you want to go? Type 'left' or 'right'. ")
if path == "right":
    path = input("You have reached a river. Do you want to swim 🏊 or wait for a boat ⛵? Type 'swin' or 'wait':")
    if path == "wait":
        path = input("You have reached an island with 3 doors. Which door you want to open? Type 'red' 🔴or 'blue' 🔵or 'green' 🟢:")
        if path == "blue":
            print("You have found the treasure and you win! 🏆")
        else:
            print("You have been eaten by beasts. Game over. 😔")
    else:
        print("You have been attacked by a trout. Game Over. 😔")
else:
    print("You have fallen into a hole. Game Over. 😔")
