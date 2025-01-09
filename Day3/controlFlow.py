#controlFlow with if, elif, else and loops
#nested if statements

print("Welcomne to the rollercoaster ride!")
height = int(input("What is your height in cm? "))
bill = 0
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        print("child tickets are $5.")
        bill = 5
    elif age <= 18:
        print("Youth tickets are $7.")
        bill = 7
    else:
        print("Adult tickets are $12.")   
        bill = 12 
        
    wants_photo = input("Do you want a photo taken? Y or N.")
    if wants_photo == "Y":
        bill += 3
        
    print(f"Your Final Bill is ${bill}")
else :
    print("Sorry, you have to grow taller before you can ride.")
    
#check if a number is odd or even - modulo operator
number = int(input("Which number do you want to check? "))
if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")

#multiple if statements
