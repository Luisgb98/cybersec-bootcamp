# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    game.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lguisado <lguisado@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/06/07 12:07:49 by lguisado          #+#    #+#              #
#    Updated: 2023/06/07 12:17:42 by lguisado         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class GotCharacter:
	'''Class representing a character in the Game of Thrones universe.'''
	def __init__(self, first_name, is_alive=True):
		self.first_name = first_name
		self.is_alive = is_alive

class Lannister(GotCharacter):
	'''Class representing the Lannister family. Or when incest goes wrong.'''
	def __init__(self, first_name=None, is_alive=True):
		super().__init__(first_name=first_name, is_alive=is_alive)
		self.family_name = "Lannister"
		self.house_words = "Hear Me Roar!"

	def print_house_words(self):
		print(self.house_words)
		
	def die(self):
		self.is_alive = False
