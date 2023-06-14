# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_map.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lguisado <lguisado@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/06/12 16:06:28 by lguisado          #+#    #+#              #
#    Updated: 2023/06/12 16:21:35 by lguisado         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_map(function_to_apply, iterable):
	"""Map the function to all elements of the iterable.
	Args:
	function_to_apply: a function taking an iterable.
	iterable: an iterable object (list, tuple, iterator).
	Return:
	An iterable.
	None if the iterable can not be used by the function.
	"""
	for i in iterable:
		yield function_to_apply(i)