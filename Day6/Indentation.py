# Indentation is very important in Python and used to define a block of code. 
# Indentation is a way to tell Python that some code is part of some other code.
# Indentation is a way of defining the structure and hierarchy of the code.
# It can be done using tabs or spaces.

# Example 1
sky = "clear"
def my_function():
    if sky == "clear":
        print("blue")
    elif sky == "cloudy":
        print("grey")
        
    print("Hello,This is outside the if-else block")
    
my_function()
print("This is outside the function")
