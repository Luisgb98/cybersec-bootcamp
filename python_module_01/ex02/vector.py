# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    vector.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lguisado <lguisado@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/06/07 12:07:54 by lguisado          #+#    #+#              #
#    Updated: 2023/06/07 12:55:34 by lguisado         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def is_range(tpl):
	if not isinstance(tpl, tuple) or len(tpl) != 2:
		return False
	if not isinstance(tpl[0], int) and isinstance(tpl[1], int) and tpl[0] < tpl[1]:
		return False
	return True

class Vector:
	def __init__(self, values):
		self.values = []
		try:
			# Check list
			if isinstance(values, list):
				print("list")
				self.values = values
				self.shape = (1, len(values))
			# Check int
			elif isinstance(values, int):
				print("int")
				if values < 0:
					print("int < 0: Invalid values for Vector")
					return
				print("int")
				self.shape = (values, 1)
				for i in range(values):
					self.values.append([float(i)])
			# Check int and float
			elif isinstance(values, (int, float)):
				print("int or float")
				self.values = values
				self.shape = (values, 1)
				for i in range(values):
					self.values.append([float(i)])
			# Check tuple
			elif is_range(values):
				print("range")
				self.shape = (values[1] - values[0], 1)
				for i in range(values[0], values[1]):
					self.values.append([float(i)])
			else:
				raise TypeError("Type not supported")
		except:
			raise ValueError("Invalid values for Vector")

	def __str__(self):
		return str(self.values)

	def dot(self, other):
		if self.shape != other.shape:
			raise ValueError("Dot product is not possible")
		result = 0
		for i in range(self.shape[0]):
			for j in range(self.shape[1]):
				print(i,j)
				result += self.values[i][j] * other.values[i][j]
		return result

	def T(self):
		if self.shape == (1,1):
			return self
		if self.shape[0] == 1:
			return Vector([[x] for x in self.values[0]])
		else:
			return Vector(self.values[::])

	def __add__(self, other):
		if self.shape != other.shape:
			raise ValueError("Vectors shapes do not match.")
		newValues = []
		for i in range(self.shape[0]):
			newRow = []
			for j in range(self.shape[1]):
				newRow.append(self.values[i][j] + other.values[i][j])
			newValues.append(newRow)
		return Vector(newValues)
	
	def __sub__(self, other):
		if self.shape != other.shape:
			raise ValueError("Vector shapes do not match.")
		newValues = []
		for i in range(self.shape[0]):
			newRow = []
			for j in range(self.shape[1]):
				newRow.append(self.values[i][j] - other.values[i][j])
			newValues.append(newRow)
		return Vector(newValues)

	def __mul__(self, other):
		if isinstance(other, (int, float)):
			newValues = []
			for i in range(self.shape[0]):
				newRow = []
				for j in range(self.shape[1]):
					newRow.append(self.values[i][j] * other)
				newValues.append(newRow)
			return Vector(newValues)
		else:
			raise TypeError("Wrong type for multiplication.")

	def __rmul__(self, other):
		return self.__mul__(other)

	def __truediv__(self, other):
		if isinstance(other, (int, float)):
			newValues = []
			for i in range(self.shape[0]):
				newRow = []
				for j in range(self.shape[1]):
					newRow.append(self.values[i][j] / other)
				newValues.append(newRow)
			return Vector(newValues)
		else:
			raise TypeError("Wrong type for division.")

	def __rtruediv__(self, other):
		raise ArithmeticError("Cannot divide by a vector.")
