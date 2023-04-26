# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    operations.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lguisado <lguisado@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/11 17:52:49 by lguisado          #+#    #+#              #
#    Updated: 2023/04/13 15:00:30 by lguisado         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def calculate(A, B):
	print("Sum:", A + B)
	print("Difference:", A - B)
	print("Product:", A * B)
	if B == 0:
		print("ERROR (division by zero)")
	else:
		print("Quotient:", A / B)
	if B == 0:
		print("ERROR (modulo by zero)")
	else:
		print("Remainder:", A % B)

def main():
	if len(sys.argv) == 3:
		try:
			int(sys.argv[1])
			int(sys.argv[2])
		except ValueError:
			print("AssertionError: argument is not an integer")
			return
		A = int(sys.argv[1])
		B = int(sys.argv[2])
		calculate(A, B)
	elif len(sys.argv) < 3:
		print("A program that takes two integers A and B as arguments and prints the result of the following operations: sum, dif, prod and div")
		print("Usage: python operations.py <number1> <number2>")
		print("Example:")
		print("	python operations.py 10 3")
	else:
		print("AssertionError: there are more than two arguments")
		print("Usage: python operations.py <number1> <number2>")
		print("Example:")
		print("	python operations.py 10 3")

if __name__ == "__main__":
    main()