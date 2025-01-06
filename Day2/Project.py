# 100 Days of Code - The Complete Python Pro Bootcamp 
# Project 2 - Tip Calculator

print("Welome to the tip calculator! ")
total_bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
split = int(input("How many people to split the bill? "))
pay = (total_bill + tip/100 * total_bill) / split 
pay = round (pay, 2)
print(f"Each person should pay: ${pay}")
