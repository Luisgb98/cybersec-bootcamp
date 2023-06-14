# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    csvreader.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lguisado <lguisado@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/06/12 18:25:37 by lguisado          #+#    #+#              #
#    Updated: 2023/06/14 14:34:38 by lguisado         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class CsvReader():
	def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
		""" Constructor of the class """
		self.filename = filename
		self.sep = sep
		self.header = header
		self.skip_top = skip_top
		self.skip_bottom = skip_bottom
		self.data = []

	def __enter__(self):
		""" Open csv file and return the object """
		try:
			self.file = open(self.filename, "r")
		except:
			print("Error: can't open file")
			return None
		for i in self.file:
			self.data.append(list(map(str.strip, i.split(self.sep))))
		if all(len(i) == len(self.data[0]) for i in self.data):
			return self
		else:
			print("Error: bad format")
			return None

	def __exit__(self, type, value, traceback):
		""" Close csv file """
		try:
			self.file.close()
		except:
			print("Error: can't close file")
			return None

	def getdata(self):
		""" Retrieves the data/records from skip_top to skip bottom.
		Return:
			nested list (list(list, list, ...)) representing the data.
		"""
		if self.header:
			self.skip_top += 1
		return self.data[self.skip_top : len(self.data) - self.skip_bottom]
	def getheader(self):
		""" Retrieves the header from csv file.
		Returns:
			list: representing the data (when self.header is True).
		None: (when self.header is False).
		"""
		if self.header == True:
			return self.data[0]
		else:
			return None