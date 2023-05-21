# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    irondome.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lguisado <lguisado@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/05/14 17:02:31 by lguisado          #+#    #+#              #
#    Updated: 2023/05/21 17:51:35 by lguisado         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import os
import sys
import math
import time
import psutil
import shutil
import argparse
import daemon
import platform
import threading
from datetime import datetime
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

path = ""
limit_cpu = 20
limit_time = 10
limit_disk_read = 10
limit_memory = 100
prev_entropy = set()

def parser_arg():
	parser = argparse.ArgumentParser(description="Stockholm")
	parser.add_argument('-g', '--generate', type=str, nargs='?', default=0, help='Create directory')
	parser.add_argument('-p', '--path', type=str, nargs='?', default=0, help='Path to check')
	args = parser.parse_args()
	return args	

class DiskReadEventHandler(FileSystemEventHandler):
	def __init__(self):
		self.count = 0
		self.create_file = None
		self.delete_file = None
		self.modified_file = None
	def on_created(self, event):
		self.count += 1
		self.create_file = event.src_path
		prev_entropy.add(calculate_entropy(self.create_file))
		ft_log_write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " - File created: {}".format(self.create_file))
	def on_deleted(self, event):
		self.count += 1
		self.delete_file = event.src_path
		ft_log_write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " - File deleted: {}".format(self.delete_file))
	def on_modified(self, event):
		self.modified_file = event.src_path
		check_entropy()
		self.count += 1

def backup():
	ft_log_write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " - Backup done")
	timestamp = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())
	shutil.copytree(path, "/root/" + "backup_" + timestamp, ignore=shutil.ignore_patterns('backup_*'))
	timer = threading.Timer(60, backup)
	timer.start()

def calculate_entropy(file_path):
	try:
		with open(file_path, "rb") as file:
			counters = {byte: 0 for byte in range(2 ** 8)}  # start all counters with zeros
			for byte in file.read():  # read in chunks for large files
				counters[byte] += 1  # increase counter for specified byte
			filesize = file.tell()  # we can get file size by reading current position
			probabilities = [counter / filesize for counter in counters.values()]  # calculate probabilities for each byte
			entropy = -sum(probability * math.log2(probability) for probability in probabilities if probability > 0)  # final sum
			return(entropy)
	except:
		return 0

def prev_check_entropy():
	for file in os.listdir(path):
		file_path = os.path.join(path, file)
		prev_entropy.add(calculate_entropy(file_path))
						
def check_entropy():
	for file in os.listdir(path):
		file_path = os.path.join(path, file)
		entropy = calculate_entropy(file_path)
		if entropy not in prev_entropy:
			ft_log_write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " - Entropy of file {} changed".format(file_path))
			if not '.swp' in file_path:
				shutil.copy(file_path, "/root/" + file_path.split('/')[-1] + "_" + datetime.now().strftime("%Y_%m_%d_%H_%M_%S"))
				ft_log_write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " - File backed up: {}".format(file_path))
			prev_entropy.add(entropy)

def	check_memory():
	memory = psutil.Process(os.getpid()).memory_info()
	mbs = memory.rss / (1024 * 1024)
	if mbs > limit_memory:
		ft_log_write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " - Memory usage is too high!")
		ft_log_write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " - Memory usage: {:.2f} MB".format(mbs))

def get_stats():
	# Log PID
	ft_log_write("Daemon PID: {}".format(os.getpid()))
	# Initialize the event handler and observer
	event_handler = DiskReadEventHandler()
	observer = Observer()
	# Recursive True to monitor subdirectories
	observer.schedule(event_handler, path=path, recursive=True)
	observer.start()
	prev_check_entropy()
	backup()
	# Monitor every x seconds
	while True:
		cpu_percent = psutil.cpu_percent()
		check_memory()
		time.sleep(limit_time)
		if event_handler.count > limit_disk_read:
			ft_log_write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " - Suspicious activity detected!")
			ft_log_write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " - Disk read count for directory {}: {}".format(path, event_handler.count))
		if cpu_percent > limit_cpu:
			ft_log_write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " - CPU usage is too high!")
			ft_log_write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " - CPU usage: {}%".format(cpu_percent))
		event_handler.count = 0

def log_start():
	if os.path.exists("/var/log/irondome/irondome.log") == False:
		try:
			os.system(f'touch /var/log/irondome/irondome.log')
		except:
			print("Error creating file /var/log/irondome/irondome.log")
			exit()
	if os.path.exists("/var/log/irondome") == True:
		try:
			os.remove("/var/log/irondome/irondome.log")
		except:
			print("Error removing file /var/log/irondome/irondome.log")
			exit()
	if os.path.exists("/var/log/irondome") == False:
		try:
			os.mkdir("/var/log/irondome")
		except:
			print("Error creating directory /var/log/irondome")
			exit()

def ft_log_write(txt):
	try:
		with open('/var/log/irondome/irondome.log', 'a') as f:
			f.write(txt + "\n")
	except:
		pass

def	generate_directory():
	for i in range(0, 300):
		file = path + "test" + str(i)
		os.system(f'touch {file}')
	print("Files created.")

def main():
	global path
	args = parser_arg()
	if (len(sys.argv) == 1):
		print("Usage: python3 irondome.py -p <path>")
		exit()
	if platform.system() != "Linux":
		print("This script is only for Linux.")
		exit()
	if os.geteuid() != 0:
		print("You need to have root privileges to run this script.")
		exit()
	if args.path is None:
		print("You need to specify a path.")
		exit()
	if args.generate is None:
		print("You need to specify a path.")
		exit()
	if args.generate:
		path = args.generate
		if path.endswith('/') == False:
			path += '/'
		generate_directory()
		exit()
	path = args.path
	if path.endswith('/') == False:
		path += '/'
	log_start()
	with daemon.DaemonContext():
		get_stats()
	# daemon = daemonize.Daemonize(app="irondome", pid="/tmp/irondome.pid" , action=get_stats)
	# daemon.start()

if __name__ == "__main__":
	main()
