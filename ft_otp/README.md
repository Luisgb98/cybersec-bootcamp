## Objective
The aim is to implement a [TOTP](https://en.wikipedia.org/wiki/Time-based_one-time_password) (Time-based One-Time Password) system, which will be capable of generating ephemeral passwords from a master key.

It will be based on the [RFC 6238](https://datatracker.ietf.org/doc/html/rfc6238).

Implement a program that allows you to register an initial password, and is capable of generating a new password each time it is requested.

## Arguments
- With the `-g` option, the program will receive as an argument a hexadecimal key of at least 64 characters. The program will safely store this key in a file called `ft_otp.key`, which will be encrypted.
```bash
python3 ft_otp.py -g [key.hex]
```
- With the `-k` option, the program will generate a new temporary password and print it to standard output.
```bash
python3 ft_otp.py -k [ft_otp.key]
```
- With the `-k` option, the program will take a decrypt key file as an argument and will decrypt the file.
```bash
python3 ft_otp.py -d [filekey.key]
```
- With the `-c` option, the program will test if the `OTP` is valid using [Pyotp](https://github.com/pyauth/pyotp) library.
```bash
python3 ft_otp.py -c [key.hex]
```
- With the `-qr` option, the program will generate a QR code with the `TOTP` to test it with `Google Authenticator`.
```bash
python3 ft_otp.py -qr [key.hex]
```

## How it works
First of all we need to check that our key is bigger than 64 hexadecimal characters. Then, we will encrypt the key with the help of `Fernet` library and we will store it in a file called `filekey.key`. This file will be used to decrypt the key and generate the `OTP` password. And the encrypted key will be stored in a file called `ft_otp.key`. Now, we decrypt the `ft_otp.key` file and we will generate the `TOTP` password using [RFC 4226](https://datatracker.ietf.org/doc/html/rfc4226#section-5). Finally, we will test if the `OTP` is valid using [Pyotp](https://github.com/pyauth/pyotp).