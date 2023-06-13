# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    book.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lguisado <lguisado@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/13 16:46:43 by lguisado          #+#    #+#              #
#    Updated: 2023/06/07 12:05:35 by lguisado         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from datetime import datetime
from recipe import Recipe

class Book:
	def __init__(self, name):
		self.name = name
		self.last_update = datetime.now()
		self.creation_date = self.last_update
		self.recipes_list = {'starter': [], 'lunch': [], 'dessert': []}
	
	def __str__(self):
		info = (
			"Name: {}\n".format(self.name)
			+ "Last update: {}\n".format(self.last_update)
			+ "Creation date: {}\n".format(self.creation_date)
			+ "Starters: {}\n".format(self.recipes_list['starter'])
			+ "Lunch: {}\n".format(self.recipes_list['lunch'])
			+ "Dessert: {}\n".format(self.recipes_list['dessert'])
			)
		return info
		
	def get_recipe_by_name(self, name):
		"""Prints a recipe with the name \texttt{name} and returns the instance"""
		# isinstance check if name is str
		if isinstance(name, str):
			for lst in self.recipes_list.values():
				for elem in lst:
					if elem.name == name:
						print(elem)
						return elem
			print("Can't find the recipe name.")
		else:
			print("Error: Name isn't a string.")
		exit()

	def get_recipes_by_types(self, recipe_type):
		"""Get all recipe names for a given recipe_type """
		if isinstance(recipe_type, str):
			if recipe_type in self.recipes_list:
				print("Recipes in {}: ".format(recipe_type))
				for elem in self.recipes_list[recipe_type]:
					print(elem.name)
				return
			else:
				print("Error: Recipe type need to be starter, lunch or dessert.")
		else:
			print("Error: That recipe type isn't a string.")
			exit()
		
	def add_recipe(self, recipe):
		"""Add a recipe to the book and update last_update"""
		if isinstance(recipe, Recipe):
			if recipe.recipe_type in self.recipes_list:
				self.recipes_list[recipe.recipe_type].append(recipe)
				self.last_update = datetime.now()
			else:
				print("Error: Recipe type need to be starter, lunch or dessert.")
		else:
			print("Error: Recipe need to be a Recipe instance.")
			exit()
