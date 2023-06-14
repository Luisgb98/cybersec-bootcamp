# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_reduce.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lguisado <lguisado@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/06/12 16:06:27 by lguisado          #+#    #+#              #
#    Updated: 2023/06/14 14:23:49 by lguisado         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_reduce(function_to_apply, iterable):
	"""Apply function of two arguments cumulatively.
	Args:
	function_to_apply: a function taking an iterable.
	iterable: an iterable object (list, tuple, iterator).
	Return:
	A value, of same type of elements in the iterable parameter.
	None if the iterable can not be used by the function.
	"""
	if isinstance(iterable, list) or isinstance(iterable, tuple):
		if len(iterable) == 0:
			return None
		result = iterable[0]
		for i in iterable[1:]:
			result = function_to_apply(result, i)
		return result