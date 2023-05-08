# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lguisado <lguisado@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/28 14:59:20 by lguisado          #+#    #+#              #
#    Updated: 2023/05/02 16:52:38 by lguisado         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

NAME    = corsair
CFLAGS  = -Wall -Wextra -Werror -Wno-deprecated-declarations

INC = /Users/lguisado/.brew/opt/openssl@3/include
LIB = /Users/lguisado/.brew/opt/openssl@3/lib

COLOUR_GREEN=\033[0;32m
COLOUR_RED=\033[0;31m
COLOUR_END=\033[0m

all: corsair

corsair: corsair.o
	@gcc corsair.o -L$(LIB) -lssl -lcrypto -o corsair
	@echo "$(COLOUR_GREEN)Compiling$(COLOUR_END)"

corsair.o: corsair.c
	@gcc -c corsair.c $(CFLAGS) -I$(INC) -o corsair.o

clean:
	@rm -rf corsair.o
	@echo "$(COLOUR_RED)Deleting all .o Files$(COLOUR_END)"
fclean: clean
	@rm -f $(NAME)
	@echo "$(COLOUR_RED)Deleting .a File$(COLOUR_END)"

re: fclean all

.PHONY: all clean fclean re