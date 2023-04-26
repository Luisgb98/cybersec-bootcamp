# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    exec.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lguisado <lguisado@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/11 14:58:01 by lguisado          #+#    #+#              #
#    Updated: 2023/04/13 14:07:19 by lguisado         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

if len(sys.argv) == 1:
	print("A program that takes a string as argument, reverses it, swaps its letters case and print the result.")
n = len(sys.argv) - 1
if n == 1:
	i = len(sys.argv[1]) - 1
	while i >= 0:
		print(sys.argv[1][i].swapcase(), end = "")
		i = i - 1
	print()
else:
	while n > 0:
		i = len(sys.argv[n]) - 1
		while i >= 0:
			print(sys.argv[n][i].swapcase(), end = "")
			i = i - 1
		if n > 1:
			print(end = " ")
		n = n - 1