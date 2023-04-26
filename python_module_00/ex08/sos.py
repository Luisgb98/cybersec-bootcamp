# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    sos.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lguisado <lguisado@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/12 18:25:48 by lguisado          #+#    #+#              #
#    Updated: 2023/04/12 19:41:36 by lguisado         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

morse = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
					'1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ' ':'/'}

def morse_translator(argv):
	argv.remove(argv[0])
	s = ' '.join(argv)
	if not all(c.isalpha() or c.isspace() or c.isnumeric() for c in s):
		print("ERROR")
		return
	for letter in s:
		print("{}".format(morse.get(letter.upper())), end=" ")
	print()

def main():
	if (len(sys.argv) < 2):
		print("ERROR")
	else:
		morse_translator(sys.argv)

if __name__ == "__main__":
	main()