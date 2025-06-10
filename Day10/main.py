# Calculator 
import art
def add(x, y):
    return x + y

def subtract(x ,y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

operations = {
    '+' : add ,
    '-' : subtract ,
    '*' : multiply , 
    '/' : divide,
    }
# print(operations["*"](4, 8))

def calculator():
    print(art.logo) 
    n1 = float(input("What's the first number: "))
    continue_d = True
    while continue_d:
        for im in operations:
            print(im)
        operation = input("Pick an operations: ")
        # operation = input("+\n-\n*\n/\nPick an operations: ")
        n2 = float(input("What's the next number: "))
        result = operations[operation](n1,n2)
        print(f"{n1} {operation} {n2} = {result}")
        should_continue = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
        if should_continue == "n":
            continue_d = False
            print("\n" * 20)
            calculator()
        elif should_continue == "y":
            n1 = result

calculator() 
