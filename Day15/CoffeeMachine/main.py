MENU =  {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = {
    "value": 0,
}

def report():
    """_summary_
    """
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources.get('milk')}ml")  #Using .get to avoid KeyError if milk is not in resources
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money['value']}")
def is_resources_sufficient(ingredients):
    """Check if there are enough resources to make the drink."""
    for item in ingredients:
        if resources.get(item,0) < ingredients[item]: # Using .get to avoid KeyError
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_coins():
    """Process the coins inserted by the user."""
    print("insert coins: ")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickels?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total
def make_coffee(drink_name, ingredient):
    """Make the coffee by using the ingredients."""
    for item in ingredient:
        resources[item] -= ingredient[item]
    print(f"Here is your {drink_name}. Enjoy!")
def coffee_machine():
    """Start the coffee machine."""
    while True:
        choice = input("What would you like? (espresso/latte/cappuccino): ")
        if choice == "off":
            break
        if choice == "report":
            report()
        elif choice in MENU:
            drink = MENU[choice]
            if is_resources_sufficient(drink["ingredients"]):
                payment = process_coins()
                if payment < drink["cost"]:
                    print("“ Sorry that's not enough money. Money refunded.” ")
                else:
                    change = round(payment - drink["cost"], 2)
                    if change > 0:
                        print(f"Here is ${change} dollars in change.")
                    money['value'] += drink["cost"]
                    make_coffee(choice, drink["ingredients"])

coffee_machine()
