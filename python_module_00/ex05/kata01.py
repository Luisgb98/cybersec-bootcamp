# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata01.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lguisado <lguisado@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/12 13:02:51 by lguisado          #+#    #+#              #
#    Updated: 2023/04/13 15:19:02 by lguisado         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

kata = {
	'Python': 'Guido van Rossum',
	'Ruby': 'Yukihiro Matsumoto',
	'PHP': 'Rasmus Lerdorf',
	'Java': 'James Gosling'
}

def	main():
	if not kata:
		print("Dictionary is empty")
		return
	for key in kata:
		print("{} was created by {}".format(key, kata[key]))

if __name__ == "__main__":
    main()