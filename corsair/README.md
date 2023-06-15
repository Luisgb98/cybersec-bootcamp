This project introduces specific concepts about the strength of the RSA algorithm and
its potential vulnerabilities. [Wiener's attack](https://en.wikipedia.org/wiki/Wiener%27s_attack) on a vulnerable RSA key.

Security in asymmetric cryptography using RSA keys is based on the premise that it is computationally very difficult to factor the two prime factors of a number. `Multiplying two prime numbers p and q to get n` is a simple operation, and its complexity does not increase dramatically as the numbers grow.

In contrast, the inverse operation, `given a number n obtain its two prime factors`, is an operation that becomes computationally infeasible when the numbers involved are large enough. To generate the key pair, the `RSA algorithm` creates a `public` and `private key` using this concept. Simplifying the generation of the keys, the randomly chosen `primes p` and `q` are multiplied to create the `modulus n` that will be used in both the `private` and `public keys`. This `module n` is public but the `prime factors p and q	` are not.

If a random number generator is weak, we can encounter a situation where the `primes p` and `q` are not random enough and can be easily factored because they have one or more factors in common. This is called a `weak key`.

## Mandatory part
- Write it in `C`.

Libraries allowed for this project:
- All functions of `<math.h>`.
- All functions of `<string.h>`.
- The [Openssl](https://github.com/openssl/openssl) library.

Create a tool that:
- Reads the public key of these certificates and get the modulus and exponent and then calculates the rest of the necessary data.
- Constructs the private key from two primes and their product, and from there, gets the symmetric key encrypted with it.
- Decrypts the message!

## How it works
First of all, we need to download the [Openssl](https://github.com/openssl/openssl) library, we can clone it or we can use `brew` to install it. To add the library to our project we need to add the following line to our `Makefile`:
```Makefile
INC = /Users/$USER/.brew/opt/openssl@3/include
LIB = /Users/$USER/.brew/opt/openssl@3/lib
```
This works on `42's iMacs` that have `openssl` installed by `brew`, but if you are using another computer you need to change the path to the library. Change `$USER` to your username.

Also, compile with the flag `-lssl -lcrypto` to link the library.
```Makefile
corsair: corsair.o
	gcc corsair.o -L$(LIB) -lssl -lcrypto -o corsair

corsair.o: corsair.c
	gcc -c corsair.c $(CFLAGS) -I$(INC) -o corsair.o
```

Then, we can use the library in our code:
```C
#include <openssl/bn.h>
#include <openssl/rsa.h>
#include <openssl/pem.h>
```
That're the libraries that we need.

### Read the public key
To read the public key we need to use the function `BIO_new_file` to open the file and then use `PEM_read_bio_RSA_PUBKEY` to read the public key and store it in a `RSA` structure.
```C
rsa -> fp = BIO_new_file(file, "r");
rsa -> rsa = PEM_read_bio_RSA_PUBKEY(rsa -> fp, NULL, NULL, NULL);
```

After that, we create a `context` to use the `BN` functions. We need to get the modulus and exponent from the `RSA` structure and store them in a `BN` structure.
```C
RSA_get0_key(rsa -> rsa1, &bn -> n1, &bn -> e, NULL);
RSA_get0_key(rsa -> rsa2, &bn -> n2, NULL, NULL);
BN_gcd(bn -> gcd, bn -> n1, bn -> n2, bn -> ctx);
```

RSA_get0_key returns from `rsa -> rsa1` the modulus and public exponent and store them in `bn -> n1` and `bn -> e`.

BN_gcd returns the greatest common divisor of `bn -> n1` and `bn -> n2` and store it in `bn -> gcd`. If `bn -> gcd` is not `1`, then we can factorize `bn -> n1` and `bn -> n2` and get the private key.

### Getting the private key
To get the private key we need to use the function `BN_div` to divide `bn -> n1` by `bn -> gcd` and store the quotient in `bn -> q1`. Then, we need to use the function `BN_sub` to get the coprime. After that, we use the function `BN_mul` to get the `totient` and then we use the function `BN_mod_inverse` to get the private exponent.
```C
BN_div(bn -> q1, NULL, bn -> n1, bn -> gcd, bn -> ctx);
BN_div(bn -> q2, NULL, bn -> n2, bn -> gcd, bn -> ctx);
BN_sub(bn -> tot1, bn -> q1, BN_value_one());
BN_sub(bn -> tot2, bn -> gcd, BN_value_one());
BN_mul(bn -> totient, bn -> tot1, bn -> tot2, bn -> ctx);
BN_mod_inverse(bn -> d, bn -> e, bn -> totient, bn -> ctx);
```

We're applying `Euler's theorem` to get the private exponent.

BN_value_one returns the value `1` as a `BN` structure.

To finish, we need to create a `RSA` structure and store the private key in it.
```C
RSA_set0_key(rsa -> private, BN_dup(bn -> n1), BN_dup(bn -> e), BN_dup(bn -> d));
```

RSA_set0_key sets the `RSA` structure with the modulus, public exponent and private exponent.

We need to use `BN_dup` to duplicate the `BN` structures to avoid leaks, explained below.

### Decrypt the message
To decrypt the message we need to use the function `RSA_private_decrypt` that needs the length of the message, the encrypted message, variable to store the decrypted message, the `RSA` structure and the padding.
```C
RSA_private_decrypt(len, enc_msg, dec, rsa -> private, RSA_PKCS1_PADDING)
```

If the function returns `-1` then the decryption failed.

### How leaks work
We have a big problem here, we need to check the official documentation of [openssl](https://www.openssl.org/docs/man1.0.2/man3/). If we go to [RSA](https://www.openssl.org/docs/man1.0.2/man3/RSA_free.html), we can see that RSA_free also free the `RSA` structure and components. So, we don't need to `BN_free` the components that `RSA` already free for us. If two `RSA` structures share the same components, we need to `BN_dup` them to avoid double free.

For example, if we do this:
```C
RSA_get0_key(rsa -> rsa1, &bn -> n1, &bn -> e, NULL);
RSA_free(rsa -> rsa1);
```
Here we don't need to `BN_free` the `bn -> n1` and `bn -> e` because `RSA_free` already free them for us.