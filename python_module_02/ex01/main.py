# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lguisado <lguisado@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/06/12 16:37:32 by lguisado          #+#    #+#              #
#    Updated: 2023/06/14 14:27:27 by lguisado         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def what_are_the_vars(*args, **kwargs):
	obj = ObjectC()
	for i in range(0, len(args)):
		setattr(obj, "var_" + str(i), args[i])
	for key, value in kwargs.items():
		if hasattr(obj, key):
			return None
		setattr(obj, key, value)
	return obj

class ObjectC(object):
	def __init__(self):
		pass

def doom_printer(obj):
	if obj is None:
		print("ERROR")
		print("end")
		return
	for attr in dir(obj):
		if attr[0] != '_':
			value = getattr(obj, attr)
			print("{}: {}".format(attr, value))
	print("end")

if __name__ == "__main__":
	obj = what_are_the_vars(7)
	doom_printer(obj)
	obj = what_are_the_vars(None, [])
	doom_printer(obj)
	obj = what_are_the_vars("ft_lol", "Hi")
	doom_printer(obj)
	obj = what_are_the_vars()
	doom_printer(obj)
	obj = what_are_the_vars(12, "Yes", [0, 0, 0], a=10, hello="world")
	doom_printer(obj)
	obj = what_are_the_vars(42, a=10, var_0="world")
	doom_printer(obj)
	obj = what_are_the_vars(42, "Yes", a=10, var_2="world")
	doom_printer(obj)
	print("-----")
	obj = what_are_the_vars(None)
	doom_printer(obj)
	obj = what_are_the_vars(lambda x: x, function=what_are_the_vars)
	doom_printer(obj)
	obj = what_are_the_vars(3, var_0=2)
	doom_printer(obj)