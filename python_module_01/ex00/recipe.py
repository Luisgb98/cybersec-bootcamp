# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lguisado <lguisado@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/13 16:46:41 by lguisado          #+#    #+#              #
#    Updated: 2023/06/06 17:58:45 by lguisado         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def check_values(name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
	if not isinstance(name, str):
		print("Error: Name isn't a string.")
		return False
	elif not isinstance(cooking_lvl, int):
		print("Error: Cooking level isn't an integer.")
		return False
	elif not isinstance(cooking_time, int):
		print("Error: Cooking time isn't an integer.")
		return False
	elif not isinstance(ingredients, list):
		print("Error: Ingredients isn't a list.")
		return False
	elif not isinstance(description, str):
		print("Error: Description isn't a string.")
		return False
	elif not isinstance(recipe_type, str):
		print("Error: Recipe type need to be starter, lunch or dessert.")
		return False
	elif recipe_type not in ['starter', 'lunch', 'dessert']:
		print("Error: Recipe type need to be starter, lunch or dessert.")
		return False
	return True

class Recipe():
	def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
		if check_values(name, cooking_lvl, cooking_time, ingredients, description, recipe_type) == True:
			self.name = name
			self.cooking_lvl = cooking_lvl
			self.cooking_time = cooking_time
			self.ingredients = ingredients
			self.description = description
			self.recipe_type = recipe_type
		else:
			print("Error: Invalid values.")
			exit()
	
	def __str__(self):
		info = (
			"Name: {}\n".format(self.name)
			+ "Cooking level: {}\n".format(self.cooking_lvl)
			+ "Cooking time: {}\n".format(self.cooking_time)
			+ "Ingredients: {}\n".format(self.ingredients)
			+ "Description: {}\n".format(self.description)
			+ "Recipe type: {}\n".format(self.recipe_type)
		)
		return info