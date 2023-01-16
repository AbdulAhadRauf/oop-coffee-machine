from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
coffee_machine = CoffeeMaker()
money = MoneyMachine()
go_on = True

while go_on:
  choice = input(f"What whould you like to have ? {menu.get_items()} \n")
  
  if choice == "report":
    coffee_machine.report()
    money.report()
  elif choice == "off":
    go_on = False
  else:
    drink = menu.find_drink(choice)
    #check if prossible
    if coffee_machine.is_resource_sufficient(drink):
      #check for the paisa
      if money.make_payment(drink.cost):
        coffee_machine.make_coffee(drink)
        
    #make coffee