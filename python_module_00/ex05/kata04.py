# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata04.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lguisado <lguisado@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/12 13:43:34 by lguisado          #+#    #+#              #
#    Updated: 2023/04/13 15:29:14 by lguisado         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

kata = (0, 4, 132.42222, 10000, 12345.67)

def	main():
	print("module_{:>02}, ex_{:>02} : {:.2f}, {:.2e}, {:.2e}".format(kata[0], kata[1], kata[2], kata[3], kata[4]))
	

if __name__ == "__main__":
	main()