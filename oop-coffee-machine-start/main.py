from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


is_on = True



money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()




while is_on:
    menu.get_items()
    choice = input("What would you like to drink? : ")


    if choice.lower() == "off":
        is_on = False
    
    elif choice.lower() == "report":
        coffee_maker.report()
        money_machine.report()
    
    else: 
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)


