# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_filter.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lguisado <lguisado@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/06/12 16:06:26 by lguisado          #+#    #+#              #
#    Updated: 2023/06/12 16:33:58 by lguisado         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_filter(function_to_apply, iterable):
	"""Filter the result of function apply to all elements of the iterable.
	Args:
	function_to_apply: a function taking an iterable.
	iterable: an iterable object (list, tuple, iterator).
	Return:
	An iterable.
	None if the iterable can not be used by the function.
	"""
	if isinstance(iterable, list) or isinstance(iterable, tuple):
		if len(iterable) == 0:
			return None
		for i in iterable:
			if function_to_apply(i):
				yield i