# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    guess.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lguisado <lguisado@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/12 19:43:09 by lguisado          #+#    #+#              #
#    Updated: 2023/04/19 13:02:52 by lguisado         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import random

def win(n, tries):
	if n == 42:
		print("The answer to the ultimate question of life, the universe and everything is 42.")
	if tries == 1:
		print("Congratulations! You got it on your first try!")
	else:
		print("Congratulations, you've got it!")
		print("You won in {} attempts!".format(tries))

def random_number():
	wine_num = random.randint(1, 99)
	tries = 0
	n = 0
	while int(n) != wine_num:
		print("What's your guess between 1 and 99?")
		n = input()
		if n == "exit":
			print("Goodbye!")
			return
		while not n.lstrip("-.e").isdigit():
			if "." or "e" in n:
				tries += 1
			try:
				int(n)
			except ValueError:
				print("That's not a number.")
				print("What's your guess between 1 and 99?")
				n = input()
		if int(n) < 0:
			print("That's a negative number.")
		elif int(n) > 99:
			print("Enter a number between 1 and 99")
		elif int(n) <= 0:
			print("Enter a number between 1 and 99")
		elif int(n) > wine_num:
			print("Too high!")
		elif int(n) < wine_num:
			print("Too low!")
		tries += 1
	win(wine_num, tries)

def main():
	print("This is an interactive guessing game!")
	print("You have to enter a number between 1 and 99 to find out the secret number.")
	print("Type 'exit' to end the game.")
	print("Good luck!")
	random_number()

if __name__ == "__main__":
	main()