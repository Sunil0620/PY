# While Loop
# The while loop in Python is used to iterate over a block of code as long as the test expression (condition) is true.
# We generally use this loop when we don't know the number of times to iterate beforehand.
# Syntax:  While something_is_true: 
             # do_something repeate dly 

count = 0
while count < 5:
    print(count)
    count += 1
# Using else statement with while loop
else:
    print("Count is greater than 5")

# Infinite loop:An infinite loop is an endless loop that will run forever unless the program is terminated.
# To create an infinite loop, we simply use the while loop and leave the test expression empty.
# # Example:
while True:
    print("This is an infinite loop")
    
