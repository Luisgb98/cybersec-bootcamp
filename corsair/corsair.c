/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   corsair.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lguisado <lguisado@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/04/27 17:10:05 by lguisado          #+#    #+#             */
/*   Updated: 2023/05/05 13:50:28 by lguisado         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "corsair.h"

void	ft_leaks(void)
{
	system("leaks -q corsair");
}

void	ft_init(t_rsa *rsa, t_bn *bn)
{
	bn -> gcd = BN_new();
	bn -> ctx = BN_CTX_new();
	bn -> q1 = BN_new();
	bn -> q2 = BN_new();
	bn -> totient = BN_new();
	bn -> tot1 = BN_new();
	bn -> tot2 = BN_new();
	bn -> d = BN_new();
	rsa -> private = RSA_new();
}

void	get_gcd(t_rsa *rsa, t_bn *bn)
{
	rsa -> rsa1 = PEM_read_bio_RSA_PUBKEY(rsa -> fp1, NULL, NULL, NULL);
	rsa -> rsa2 = PEM_read_bio_RSA_PUBKEY(rsa -> fp2, NULL, NULL, NULL);
	if (!rsa -> rsa1 || !rsa -> rsa2)
	{
		printf("Can't read certificates\n");
		exit(0);
	}
	printf("---- PUBLIC RSA 1: ----\n");
	RSA_print_fp(stdout, rsa -> rsa1, 0);
	printf("\n---- PUBLIC RSA 2: ----\n");
	RSA_print_fp(stdout, rsa -> rsa2, 0);
	RSA_get0_key(rsa -> rsa1, &bn -> n1, &bn -> e, NULL);
	RSA_get0_key(rsa -> rsa2, &bn -> n2, NULL, NULL);
	printf("\n---- GCD: ----\n");
	BN_gcd(bn -> gcd, bn -> n1, bn -> n2, bn -> ctx);
	BN_print_fp(stdout, bn -> gcd);
}

void	get_private(t_rsa *rsa, t_bn *bn)
{
	BN_div(bn -> q1, NULL, bn -> n1, bn -> gcd, bn -> ctx);
	BN_div(bn -> q2, NULL, bn -> n2, bn -> gcd, bn -> ctx);
	BN_sub(bn -> tot1, bn -> q1, BN_value_one());
	BN_sub(bn -> tot2, bn -> gcd, BN_value_one());
	BN_mul(bn -> totient, bn -> tot1, bn -> tot2, bn -> ctx);
	BN_mod_inverse(bn -> d, bn -> e, bn -> totient, bn -> ctx);
	RSA_set0_key(rsa -> private, BN_dup(bn -> n1),
		BN_dup(bn -> e), BN_dup(bn -> d));
	printf("\n---- PRIVATE KEY: ----\n");
	RSA_print_fp(stdout, rsa -> private, 0);
	RSA_set0_factors(rsa -> rsa1, bn -> gcd, bn -> q1);
	RSA_set0_factors(rsa -> rsa2, bn -> gcd, bn -> q2);
}

void	decrypt_file(t_rsa *rsa, char *file)
{
	unsigned char	*enc_msg;
	unsigned char	*dec;
	int				fd;
	int				len;

	enc_msg = malloc(sizeof(unsigned char) * BUFFER_SIZE);
	dec = malloc(sizeof(unsigned char) * BUFFER_SIZE);
	fd = open(file, O_RDONLY);
	if (fd < 0)
	{
		printf("Can't read encrypted file\n");
		exit(0);
	}
	len = read(fd, enc_msg, BUFFER_SIZE);
	if (RSA_private_decrypt(len, enc_msg, dec, rsa -> private,
			RSA_PKCS1_PADDING) < 0)
	{
		printf("Wrong decrypt key\n");
		exit(0);
	}
	printf("---- FILE ENCRYPTED ---- \n%s\n", enc_msg);
	printf("---- FILE DECRYPTED ---- \n%s", dec);
	free(enc_msg);
	free(dec);
	close(fd);
}

void	ft_free(t_rsa *rsa, t_bn *bn)
{
	BIO_free(rsa -> fp1);
	BIO_free(rsa -> fp2);
	RSA_free(rsa -> rsa1);
	RSA_free(rsa -> rsa2);
	RSA_free(rsa -> private);
	BN_CTX_free(bn -> ctx);
	BN_free(bn -> totient);
	BN_free(bn -> tot1);
	BN_free(bn -> tot2);
	BN_free(bn -> d);
	free(rsa);
	free(bn);
}

void	ft_free_no_vuln(t_bn *bn)
{
	printf("\nNo vulnerable\n");
	BN_free(bn -> gcd);
	BN_free(bn -> q1);
	BN_free(bn -> q2);
}

int	main(int argc, char **argv)
{
	t_rsa	*rsa;
	t_bn	*bn;

	atexit(ft_leaks);
	if (argc < 4 || argc > 4)
		printf("Provide 2 certificates and file to decrypt\n");
	else
	{
		rsa = malloc(sizeof(t_rsa));
		bn = malloc(sizeof(t_bn));
		rsa -> fp1 = BIO_new_file(argv[1], "r");
		rsa -> fp2 = BIO_new_file(argv[2], "r");
		ft_init(rsa, bn);
		get_gcd(rsa, bn);
		if (BN_is_one(bn -> gcd))
			ft_free_no_vuln(bn);
		else
		{
			get_private(rsa, bn);
			decrypt_file(rsa, argv[3]);
		}
		ft_free(rsa, bn);
	}
}
