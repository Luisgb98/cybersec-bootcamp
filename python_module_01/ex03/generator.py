# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    generator.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lguisado <lguisado@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/06/07 12:08:00 by lguisado          #+#    #+#              #
#    Updated: 2023/06/07 13:04:48 by lguisado         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import random

def generator(text, sep=" ", option=None):
	''' Splits the text according to sep value and yield the substrings.
	option precise if a action is performed to the substrings before it is yielded. '''
	if not isinstance(text, str):
		raise TypeError("text must be a string")
	if option and option not in ["shuffle", "unique", "ordered"]:
		raise ValueError("option is not valid, must be 'shuffle', 'unique' or 'ordered'")
	words = text.split(sep)
	if option == 'shuffle':
		words = shuffle_list(words)
	elif option == 'unique':
		words = list(set(words))
	elif option == 'ordered':
		words = sorted(words)
	for word in words:
		yield word

def shuffle_list(lst):
    ''' Shuffles a list and return it. '''
    shuffleList = lst[:]
    for i in range(len(shuffleList) - 1, 0, -1):
        j = random.randint(0, i)
        shuffleList[i], shuffleList[j] = shuffleList[j], shuffleList[i]
    return shuffleList
