from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee = CoffeeMaker()
money = MoneyMachine()
drink = Menu()

global prompt
prompt = ""



def question():
    print("What would you like? " + drink.get_items())

def selection(prompt):
        drinks = drink.find_drink(prompt)
        if coffee.is_resource_sufficient(drinks) and money.make_payment(drinks.cost):
            coffee.make_coffee(drinks)
    


def report():
    coffee.report()
    money.report()

while prompt != "off":
    question()
    prompt = input()

    if prompt == "report":
        report()
    
    if prompt == "espresso" or prompt == "latte" or prompt == "cappuccino":
        selection(prompt)
