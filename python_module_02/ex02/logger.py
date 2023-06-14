# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    logger.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lguisado <lguisado@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/06/12 17:58:51 by lguisado          #+#    #+#              #
#    Updated: 2023/06/13 18:39:50 by lguisado         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import time
from random import randint
import os

def log(func):
	def wrapper(*args, **kwargs):
		user = os.getlogin()
		start = time.time()
		run = func(*args, **kwargs)
		end = time.time()
		with open("logger.log", "a") as file:
			file.write("({})Running: {:20}[ exec-time = {:.3f} ms ]\n".format(user,func.__name__, (end - start) * 1000))
		return run
	return wrapper

class CoffeeMachine():
	water_level = 100
	@log
	def start_machine(self):
		if self.water_level > 20:
			return True
		else:
			print("Please add water!")
			return False

	@log
	def boil_water(self):
		return "boiling..."

	@log
	def make_coffee(self):
		if self.start_machine():
			for _ in range(20):
				time.sleep(0.1)
				self.water_level -= 1
			print(self.boil_water())
			print("Coffee is ready!")

	@log
	def add_water(self, water_level):
		time.sleep(randint(1, 5))
		self.water_level += water_level
		print("Blub blub blub...")

if __name__ == "__main__":
	try:
		os.remove("logger.log")
	except:
		pass
	machine = CoffeeMachine()
	for i in range(0, 5):
		machine.make_coffee()
	machine.make_coffee()
	machine.add_water(70)