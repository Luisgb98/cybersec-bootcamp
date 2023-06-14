# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    loading.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lguisado <lguisado@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/12 20:47:30 by lguisado          #+#    #+#              #
#    Updated: 2023/04/18 19:12:34 by lguisado         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import time

def ft_progress(lst):
	count = len(lst)
	size = 60
	prefix = ""
	init = time.time()
	def show(loaded):
		et = time.time() - init
		if et == 0:
			speed = 0
		else:
			speed = (loaded/et)
		if speed == 0:
			eta = 0
		else:
			eta = (count/speed)
		x = int(size*loaded/count)
		percentage = round(100.0 * loaded/count, 1)
		print(f"ETA: {eta:.2f} {prefix}[{percentage}%][{u'='*x}>{(' '*(size-x))}] {loaded}/{count} | elapsed time {et:.2f}" , end='\r', file=print(end=""), flush=True)
	show(0)	
	for i, item in enumerate(lst):
		yield item
		show(i+1)
	print("\n", flush=True, file=print(end=""))

# def main():
# 	listy = range(1000)
# 	ret = 0
# 	for elem in ft_progress(listy):
# 		ret += (elem + 3) % 5
# 		time.sleep(0.01)
# 	print()
# 	print(ret)

# if __name__ == "__main__":
# 	main()