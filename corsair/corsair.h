/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   corsair.h                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lguisado <lguisado@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/04/27 17:10:12 by lguisado          #+#    #+#             */
/*   Updated: 2023/05/05 13:45:23 by lguisado         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef CORSAIR_H
# define CORSAIR_H

# include <math.h>
# include <string.h>
# include <stdio.h>
# include <fcntl.h>
# include <stdlib.h>
# include <unistd.h>
/* OPENSSL LIBRARY */
# include <openssl/bn.h>
# include <openssl/rsa.h>
# include <openssl/pem.h>

# ifndef BUFFER_SIZE
#  define BUFFER_SIZE 1024
# endif

typedef struct s_rsa
{
	RSA		*rsa1;
	RSA		*rsa2;
	RSA		*private;
	BIO		*fp1;
	BIO		*fp2;
}	t_rsa;

typedef struct s_bn
{
	const BIGNUM	*n1;
	const BIGNUM	*n2;
	const BIGNUM	*e;
	BIGNUM			*d;
	BN_CTX			*ctx;
	BIGNUM			*gcd;
	BIGNUM			*q1;
	BIGNUM			*q2;
	BIGNUM			*totient;
	BIGNUM			*tot1;
	BIGNUM			*tot2;
}	t_bn;

#endif