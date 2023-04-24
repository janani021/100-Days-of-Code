from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine= MoneyMachine()
coffee_maker = CoffeeMaker()
menu=Menu()
flag = True

while flag:
    options=menu.get_items()
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        flag = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink=menu.find_drink(choice)
        if(coffee_maker.is_resource_sufficient(drink)):
           if(money_machine.make_payment(drink.cost)):
               coffee_maker.make_coffee(drink)