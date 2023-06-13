# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lguisado <lguisado@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/13 16:46:39 by lguisado          #+#    #+#              #
#    Updated: 2023/06/07 12:07:30 by lguisado         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from book import Book
from recipe import Recipe

def main():
	book = Book("My book")
	recipe = Recipe("My recipe", 1, 10, ["ingredient1", "ingredient2"], "My description", "starter")
	recipe2 = Recipe("My recipe2", 2, 20, ["ingredient1", "ingredient2"], "My description", "lunch")
	recipe3 = Recipe("My recipe3", 3, 30, ["ingredient1", "ingredient2"], "My description", "dessert")
	book.add_recipe(recipe)
	book.add_recipe(recipe2)
	book.add_recipe(recipe3)
	book.get_recipe_by_name("My recipe")

if __name__ == "__main__":
	main()