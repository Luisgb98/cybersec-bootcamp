# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata00.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lguisado <lguisado@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/11 18:51:51 by lguisado          #+#    #+#              #
#    Updated: 2023/04/13 15:04:04 by lguisado         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

kata = ()

def main():
	if len(kata) == 0:
		print("Tuple is empty")
		return
	for n in kata:
		if not str(n).lstrip("-").isdigit():
			print("Tuple can only be filled with integers")
			return
	joined = ", ".join(map(str, kata))
	print("The {} numbers are: {}".format(len(kata), joined))

if __name__ == "__main__":
    main()