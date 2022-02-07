from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffeeMaker = CoffeeMaker()
moneyMachine = MoneyMachine()
off = False
while not off:
    choice = input(f"What would you like? {menu.get_items()}:")
    if choice == "report":
        coffeeMaker.report()
    elif choice == "off":
        off = True
    else:
        item = menu.find_drink(choice)
        if item:
            if coffeeMaker.is_resource_sufficient(item) and moneyMachine.make_payment(item.cost):
                coffeeMaker.make_coffee(item)
