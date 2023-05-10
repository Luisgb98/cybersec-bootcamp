/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   vulnerable.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lguisado <lguisado@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/05/08 16:23:34 by lguisado          #+#    #+#             */
/*   Updated: 2023/05/10 17:11:07 by lguisado         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#include <string.h>

void	vulnerable(char *argv)
{
	char	buffer[64];

	strcpy(buffer, argv);
	printf("%s", buffer);
}

int	main(int argc, char **argv)
{
	vulnerable(argv[1]);
}
