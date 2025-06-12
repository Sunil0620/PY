from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

print("Welcome to the Coffee Machine!")
coffee_maker = CoffeeMaker()    # Create an instance(obj) of CoffeeMaker
money_machine = MoneyMachine()  # Create an instance of MoneyMachine
menu = Menu()                   # Create an instance of Menu
IS_ON = True

while IS_ON:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        IS_ON = False
    elif choice == "report":
        coffee_maker.report()    # Call the report method of CoffeeMaker
        money_machine.report()   # Call the report method of MoneyMachine
    else:
        drink = menu.find_drink(choice)
        if drink:
            if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
        else:
            print("Sorry, you can choose only from the menu.")
            continue
    print("Thank you for using the Coffee Machine!")