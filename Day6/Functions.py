# 1. Function to print a message
# 2. Function to add two numbers and return the sum and product
# 3. Function to calculate the factorial of a number

def my_function():
    print("Hello, welcome to the My functions!")
    
def add_numbers(a, b):
    sum = a + b
    product = a * b
    return sum, product 

def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Calling functions
my_function()
sum, product = add_numbers(2, 3) # Unpacking the tuple
print("Sum:", sum)
print("Product:", product)
print("Factorial of 5:", factorial(5))
my_function()
sum, product = add_numbers(2, 3) # Unpacking the tuple
print("Sum:", sum)
print("Product:", product)
print("Factorial of 5:", factorial(5))
