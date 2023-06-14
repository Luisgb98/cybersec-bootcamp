# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    TinyStatistician.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lguisado <lguisado@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/06/13 18:08:17 by lguisado          #+#    #+#              #
#    Updated: 2023/06/13 18:28:10 by lguisado         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class TinyStatistician:
	def mean(self, x) -> float:
		if not x:
			return None

		total = 0

		for num in x:
			total += num

		mean = total / len(x)

		return mean

	def median(self, x: list) -> float:
		if not x:
			return None

		sorted_x = sorted(x)
		n = len(sorted_x)
		mid_index = n // 2

		if n % 2 == 0:
			median = (sorted_x[mid_index - 1] + sorted_x[mid_index]) / 2
		else:
			median = sorted_x[mid_index]

		return median

	def quartiles(self, x):
		if not x:
			return None
		sorted_x = sorted(x)
		n = len(sorted_x)

		q1_index = n // 4
		q3_index = 3 * n // 4

		q1 = sorted_x[q1_index]
		q3 = sorted_x[q3_index]

		return q1, q3

	def var(self, x) -> float:
		if not x:
			return None

		mean = sum(x) / len(x)
		total = 0

		for num in x:
			total += (num - mean) ** 2

		variance = total / len(x)

		return variance

	def std(self, x) -> float:
		if not x:
			return None

		mean = sum(x) / len(x)
		total = 0

		for num in x:
			total += (num - mean) ** 2

		variance = total / len(x)
		standard_deviation = variance ** 0.5
		
		return standard_deviation
