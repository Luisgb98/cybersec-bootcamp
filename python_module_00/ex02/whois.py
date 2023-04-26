# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    whois.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lguisado <lguisado@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/11 14:58:04 by lguisado          #+#    #+#              #
#    Updated: 2023/04/13 14:09:34 by lguisado         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

isint = True
if len(sys.argv) > 2:
	print("AssertionError: more than one argument are provided")
elif len(sys.argv) == 1:
	print("A program that takes a number as argument, checks whether it is odd, even or zero, and print the result.")
else:
	try:
		int(sys.argv[1])
	except ValueError:
		isint = False
	if isint == False:
		print("AssertionError: argument is not an integer")
	else:
		n = int(sys.argv[1])
		if n == 0:
			print("I'm Zero.")
		elif n % 2 == 1:
			print("I'm Odd.")
		else:
			print("I'm Even.")