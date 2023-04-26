# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lguisado <lguisado@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/12 14:15:51 by lguisado          #+#    #+#              #
#    Updated: 2023/04/17 13:58:32 by lguisado         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

cookbook = {
	'Sandwich' : {
		'ingredients' : ["ham", "bread", "cheese", "tomatoes"],
		'meal' : 'lunch',
		'prep_time' : '10'
	},
	'Cake' : {
		'ingredients' : ["flour", "sugar", "eggs"],
		'meal' : 'dessert',
		'prep_time' : '60'
	},
	'Salad' : {
		'ingredients' : ["avocado", "arugula", "tomatoes", "spinach"],
		'meal' : 'lunch',
		'prep_time' : '15'
	}
}

def print_recipes():
	print("\nList of recipes:")
	if not cookbook:
		print("No recipes available")
	for key in cookbook.keys():
		print("  {}".format(key))

def	print_details():
	print("\nPlease enter a recipe name to get its details:")
	recipe = input()
	for key in cookbook.keys():
		if recipe == key:
			print("Recipe for {}:".format(recipe))
			print("  Ingredients list: {}".format(cookbook[recipe].get("ingredients")))
			print("  To be eaten for {}.".format(cookbook[recipe].get("meal")))
			print("  Takes {} minutes of cooking.".format(cookbook[recipe].get("prep_time")))
	try:
		cookbook[recipe]
	except KeyError:
		print("This recipe doesn't exist, this is a list of recipes avaibles")
		print_recipes()
		if not cookbook:
			cookbook_menu()
		else:
			print_details()

def	delete_recipe():
	print("\nPlease enter a recipe name to delete it:")
	recipe = input()
	if recipe in cookbook.keys():
		del(cookbook[recipe])
		print("{} has been deleted".format(recipe))
	else:
		print("This recipe doesn't exist, this is a list of recipes avaibles")
		print_recipes()
		if not cookbook:
			cookbook_menu()
		else:
			delete_recipe()

def add_recipe():
	print("\nPlease enter a name:")
	name = input()
	while not name:
		print("\nPlease enter a valid name:")
		name = input()
	print("Please enter some ingredients:")
	ingredients = []
	ingredient = input()
	while not ingredient:
		print("Error, please enter some ingredients")
		ingredient = input()
	ingredients.append(ingredient)	
	while ingredient:
		ingredient = input()
		if ingredient:
			ingredients.append(ingredient)
	# ingredients = [item for item in input().split()]
	print("Please enter meal type:")
	meal_type = input()
	while not meal_type:
		print("\nPlease enter a valid meal type:")
		meal_type = input()
	print("Please enter a preparation time:")
	time = input()
	while not time.isdigit():
		try:
			int(time)
		except ValueError:
			print("Please enter the number of minutes:")
			time = input()
	cookbook[name] = {'ingredients': ingredients, 'meal': meal_type, 'prep_time': time}
	print("Recipe added")

def	print_options():
	print("\nList of available option:")
	print("  1: Add a recipe")
	print("  2: Delete a recipe")
	print("  3: Print a recipe")
	print("  4: Print the cookbook")
	print("  5: Quit\n")
	cookbook_menu()

def cookbook_menu():
	print("Please select an option:")
	menu = input()
	if menu == '1':
		add_recipe()
		cookbook_menu()
	elif menu == '2':
		delete_recipe()
		cookbook_menu()
	elif menu == '3':
		print_details()
		cookbook_menu()
	elif menu == '4':
		print_recipes()
		cookbook_menu()
	elif menu == '5':
		print("\nCookbook closed. Goodbye !")
		exit()
	else:
		print("Sorry, this option does not exist.")
		print_options()
		cookbook_menu()

def	main():
	print("Welcome to the Python Cookbook !")
	print_options()
	cookbook_menu()

if __name__ == "__main__":
	main()