# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_otp.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lguisado <lguisado@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/20 17:10:41 by lguisado          #+#    #+#              #
#    Updated: 2023/04/25 19:43:03 by lguisado         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import argparse
import hashlib
import hmac
import math
import time
import struct
import pyotp
import qrcode
from cryptography.fernet import Fernet

def parser_arg():
	parser = argparse.ArgumentParser(description="One-Time Password Algorithm")
	parser.add_argument('-g', '--generate', type=str, help='Take a hex file with 64 chars and encrypted it in a ft_otp.key file')
	parser.add_argument('-k', '--key',type=str, help='Generate a temp password and show it on console')
	parser.add_argument('-d', '--decrypt',type=str, help='Decrypt ft_otp.key')
	parser.add_argument('-c', '--check',type=str, help='Check TOTP with pyotp library')
	parser.add_argument('-qr', '--qr',type=str, help='Generate a QR Code for Google Authenticator')
	args = parser.parse_args()
	return args

def generate_totp(key_file):
	with open(key_file, 'r') as f:
		hex_read = f.read()
	try:
		key_bytes = bytearray.fromhex(hex_read)
	except:
		print("Key encrypted")
		exit()
	actual_sec = math.floor(time.time())
	time_between = 30
	key_time = math.floor(actual_sec / time_between)
	time_bytes = struct.pack(">Q", key_time)
	hash_code = hmac.digest(key_bytes, time_bytes, hashlib.sha1)
	offset = hash_code[len(hash_code) - 1] & 0xf
	binary = ((hash_code[offset] & 0x7f) << 24) | ((hash_code[offset + 1] & 0xff) << 16) | ((hash_code[offset + 2] & 0xff) << 8) | (hash_code[offset + 3] & 0xff);
	code_key = binary % 1000000
	print("TOTP: {:06d}".format(code_key))

def encrypt_key(hex_read):
	with open('ft_otp.key', 'w') as f:
		f.write(hex_read)
	key = Fernet.generate_key()
	with open('filekey.key', 'wb') as filekey:
		filekey.write(key)

def encrypt_file():
	with open('filekey.key', 'rb') as filekey:
		key = filekey.read()
	decode = Fernet(key)
	with open('ft_otp.key', 'rb') as f:
		original = f.read()
	encrypted = decode.encrypt(original)
	with open('ft_otp.key', 'wb') as encrypted_file:
		encrypted_file.write(encrypted)

def decrypt_file():
	with open('filekey.key', 'rb') as filekey:
		key = filekey.read()
	decode = Fernet(key)
	with open('ft_otp.key', 'rb') as encrypted_file:
		encrypted = encrypted_file.read()
	decrypted = decode.decrypt(encrypted)
	with open('ft_otp.key', 'wb') as decrypted_file:
		decrypted_file.write(decrypted)

def read_file(f):
	if ".hex" in f:
		with open(f, 'r') as file_to_read:
			hex_read = file_to_read.read()
			if len(hex_read) < 64:
				error()
			try:
				int(hex_read, 16)
			except ValueError:
				error()
		return hex_read
	else:
		error()

def check_totp(my_totp):
	toread = 'IFXHIZLTKF2WKTTBMRQUG33NN5CXG5DBNZGG642NMFYXK2LOMFZSYVTBNVXXGQKIMFRWK4TON5ZVK3TBIZXXI32PIFWGO32ON5CGC3DFIFUGSTLBOF2WS3TB'
	totp = pyotp.TOTP(toread)
	print('PYOTP: {}'.format(totp.now()))

def generate_qr():
	path = 'otpauth://totp/TOTP%20lguisado:lguisado%40student.42malaga.com?secret=IFXHIZLTKF2WKTTBMRQUG33NN5CXG5DBNZGG642NMFYXK2LOMFZSYVTBNVXXGQKIMFRWK4TON5ZVK3TBIZXXI32PIFWGO32ON5CGC3DFIFUGSTLBOF2WS3TB&issuer=TOTP%20lguisado'
	qrcode.make(path).save('qr.png')

def error():
	print("Error: key must be 64 hexadecimal characters.")
	exit()

if __name__ == "__main__":
	args = parser_arg()
	if args.generate:
		hex_read = read_file(args.generate)
		encrypt_key(hex_read)
		encrypt_file()
	elif args.decrypt:
		decrypt_file()
	elif args.key:
		generate_totp(args.key)
	elif args.check:
		totp = generate_totp(args.check)
		check_totp(totp)
	elif args.qr:
		generate_qr()