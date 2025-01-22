# Project 5 - Password Generator
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 
'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 
'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',]
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+',]

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Easy Level
# password = ""

# for char in range(0, nr_letters):
#     password += random.choice(letters)
    
# for char in range(0, nr_symbols):
#     password += random.choice(symbols)
    
# for char in range(0, nr_numbers):
#     password += random.choice(numbers)
    
# print(password)
# the append() function is a built-in fn used to add an item to the end of a list. 

# Hard Level
password_list = [] # empty list
for char in range(0,nr_letters):
    password_list.append(random.choice(letters)) # append adds to the list
    # password += random.choice(letters)

for char in range(0,nr_symbols):
    password_list.append(random.choice(symbols))
    # password += random.choice(symbols)
    
for char in range(0,nr_numbers):
    password_list.append(random.choice(numbers))
    # password += random.choice(numbers)

# shuffle() function is used to shuffle the list
print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
    password += char
print(f"Your password is: {password}")
