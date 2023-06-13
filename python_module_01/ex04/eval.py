# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    eval.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lguisado <lguisado@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/06/07 12:08:08 by lguisado          #+#    #+#              #
#    Updated: 2023/06/07 13:21:53 by lguisado         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Evaluator:
	''' Compute the sum of the lengths of every words of
	a given list weighted by a list of coefficinents coefs. '''
	@staticmethod
	def zip_evaluate(coefs, words):
		if len(coefs) != len(words):
			return -1
		return sum(coef * len(word) for coef, word in zip(coefs, words))

	@staticmethod
	def enumerate_evaluate(coefs, words):
		if len(coefs) != len(words):
			return -1
		return sum(coefs[i] * len(words[i]) for i, _ in enumerate(words))
