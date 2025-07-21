from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine



menu = Menu()
process = CoffeeMaker()
manu = MoneyMachine()


end = False

while end == False:
	items = menu.get_items()         # get the items from the list 
	print(items)
	order = input("Which drink you wanna choose?")
	drink = menu.find_drink(order)  # is the drink in the list ???
	if process.is_resource_sufficient(drink):
		cost = drink.cost   
		print(f"{cost} €")
		check = manu.make_payment(cost)

		if check == True:
			process.make_coffee(drink)
		else:
			end = True


		
	
	
	  
	


	







	

