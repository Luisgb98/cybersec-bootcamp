# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    filterwords.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lguisado <lguisado@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/12 17:34:52 by lguisado          #+#    #+#              #
#    Updated: 2023/04/13 16:20:40 by lguisado         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import string

def check_error(n):
	try:
		int(n)
	except ValueError:
		print("ERROR")
		return 0

def	filtering(s, n):
	old_list = []
	for i in s:
		if i in string.punctuation:
			s = s.replace(i, "")
	old_list = s.strip().split(" ")
	new_list = [x for x in old_list if len(x) > int(n)]
	print(new_list)

def	main():
	if (len(sys.argv) == 3):
		if check_error(sys.argv[2]) != 0:
			filtering(sys.argv[1], sys.argv[2])
	else:
		print("ERROR")

if __name__ == "__main__":
	main()