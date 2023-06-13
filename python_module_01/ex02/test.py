# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lguisado <lguisado@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/06/07 12:20:40 by lguisado          #+#    #+#              #
#    Updated: 2023/06/07 12:23:46 by lguisado         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from vector import Vector

def main():
	### # 01.02.00
	print(Vector([1. , 2e-3, 3.14, 5.]).values)

	### # 01.02.01
	print(Vector(4).values)

	### # 01.02.02
	print(Vector(-1))

	### # 01.02.03
	print(Vector((10, 12)).values)

	### # 01.02.04
	print(Vector((3, 1)).values)

	### # 01.02.05
	v = Vector((1, 1))
	print(v.values)

	### # 01.02.06
	print(Vector((4, 7.1)))

	### # 01.02.07
	v = Vector(4)
	print(v.values)

	### # 01.02.08
	print(print(v * 4))

	### # 01.02.09
	print(print(4.0 * v))

	### # 01.02.10
	print(v * "hi")

	### # 01.02.11
	v = Vector(4)
	v2 = Vector([[1.0], [1.0], [1.0], [1.0]])
	print((v + v2).values)

	### # 01.02.12
	print(v + Vector([0.0, 0.0, 0.0, 0.0]))

	### # 01.02.13
	print(v + "hello")

	### # 01.02.14
	print(v + None)

	### # 01.02.15
	print((v - v2).values != (v2 - v).values)

	### # 01.02.16
	print(Vector(4) / 2)

	### # 01.02.17
	print(Vector(4) / 3.14)

	### # 01.02.18
	print(Vector(4) / 0)

	### # 01.02.19
	print(Vector(4) / None)

	### # 01.02.20
	print(None / Vector(4))

	### # 01.02.21
	print(3 / Vector(3))

if __name__ == "__main__":
	main()