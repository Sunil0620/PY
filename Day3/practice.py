#Pizza order program

print("Welcome to Python Pizza Deliveries!")
bill = 0
size = input("What size pizza do you want? S, M, or L\n")
if size == "S":
    bill = 15
    print("Small Pizza: $15")
elif size == "M":
    bill = 20
    print("Medium Pizza: $20")
elif size == "L":
    bill = 25
    print("Large Pizza: $25")
    
    pepperoni = input("Do you want pepperoni? Y or N\n")
    if pepperoni == "Y":
        if size == "S":
            bill += 2
        else:
            bill += 3
            
    extra_cheese = input("Do you want extra cheese? Y or N\n")
    if extra_cheese == "Y":
        bill += 1
    print(f"Your final bill is: ${bill}.")
else :
    print("Invalid input")
        #This is the final code of the pizza order program
    