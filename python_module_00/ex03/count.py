# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    count.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lguisado <lguisado@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/11 15:47:28 by lguisado          #+#    #+#              #
#    Updated: 2023/04/11 17:50:56 by lguisado         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import string

def text_analyzer(text = ""):
	"""This function counts the number of upper characters, lower characters, punctuation and spaces in a given text."""
	if type(text) != str:
		print("AssertionError: argument is not a string")
	else:
		if text == "":
			text = input("What is the text to analyze?\n")
		i = 0
		strlen = len(text)
		upper = 0
		lower = 0
		mark = 0
		space = 0
		while strlen > 0:
			if text[i].isupper():
				upper += 1
			elif text[i].islower():
				lower += 1
			elif text[i] == " ":
				space += 1
			else:
				for j in string.punctuation:
					if j == text[i]:
						mark += 1
			i += 1
			strlen -= 1
		print(f"The text contains {len(text)} character(s):")
		print(f"- {upper} upper letter(s)")
		print(f"- {lower} lower letter(s)")
		print(f"- {mark} punctuation mark(s)")
		print(f"- {space} space(s)")

def main():
	if len(sys.argv) == 1:
		text_analyzer()
	elif len(sys.argv) > 2:
		print("AssertionError: more than one argument are provided")
	else:
		if sys.argv[1].isnumeric():
			print("AssertionError: argument is not a string")
		else:
			text_analyzer(sys.argv[1])

if __name__ == "__main__":
    main()