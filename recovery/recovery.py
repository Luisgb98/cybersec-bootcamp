# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recovery.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lguisado <lguisado@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/05/21 18:29:23 by lguisado          #+#    #+#              #
#    Updated: 2023/05/23 19:46:40 by lguisado         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import os
import wmi
import psutil
import winreg
import sqlite3
import argparse
import tempfile
import win32com.client
import tkinter as tk
import tkinter.ttk as ttk
from datetime import datetime, timedelta

actual_time = datetime.now()
timerange = actual_time - timedelta(days=1)

def validate_date(date_str):
	try:
		date_obj = datetime.strptime(date_str, "%Y-%m-%d")	
		return date_obj
	except ValueError:
		try:
			date_obj = datetime.strptime(date_str, "%d-%m-%Y")
			return date_obj
		except ValueError:
			raise argparse.ArgumentTypeError("Invalid date format. Expected format: YYYY-MM-DD or DD-MM-YYYY")

def parse_arguments():
	parser = argparse.ArgumentParser(description="Get information about the system with a time range")
	parser.add_argument('-t', '--timerange', type=validate_date, help='The date in the format YYYY-MM-DD')
	parser.add_argument('-d', '--directorytree', nargs='?', default=0, help='Display the root directory tree')
	args = parser.parse_args()
	return args

def check_registry():
	path = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run"
	try:
		key = winreg.HKEY_LOCAL_MACHINE
		registry_key = winreg.OpenKey(key, path, 0, winreg.KEY_READ)
		modification_timestamp = winreg.QueryInfoKey(key)[2]
		# Epoch time for Windows is 11644473600
		last = modification_timestamp/10000000 - 11644473600
		last_date = datetime.fromtimestamp(last)
		winreg.CloseKey(registry_key)
		print("--- Registry: ---\n")
		if timerange <= last_date <= actual_time:
			print("Last Modified: {} - CurrentVersionRun: {}".format(last_date.strftime("%Y-%m-%d %H:%M:%S"), registry_key))
		else:
			print("There is no modification in the registry in the time range given")
	except WindowsError:
		print("Error while reading registry")

def check_recent_files():
	recent_folder_path = os.path.expanduser("~\\AppData\\Roaming\\Microsoft\\Windows\\Recent")
	recent_files = []
	try:
		for file in os.listdir(recent_folder_path):
			if not file.endswith(".lnk"):
				continue
			file_path = os.path.join(recent_folder_path, file)
			modified_time = datetime.fromtimestamp(os.path.getmtime(file_path))
			if timerange <= modified_time <= actual_time:
				recent_files.append({
					'date': modified_time,
					'file': file.strip(".lnk")})
	except:
		pass
	recent_files = sorted(recent_files, key=lambda d: d['date'])
	print("\n--- Recent files: ---\n")
	for recent in recent_files:
		date_formatted = recent['date'].strftime("%Y-%m-%d %H:%M:%S")
		print("Date: {} | File: {}".format(date_formatted, recent['file']))

def check_temp_files():
	# Get the path to the temporary directory
	temp_dir = tempfile.gettempdir()

	# List all files in the temporary directory
	file_list = os.listdir(temp_dir)

	# Retrieve the datetime for each file
	temp_list = []
	for file_name in file_list:
		file_path = os.path.join(temp_dir, file_name)
		creation_time = datetime.fromtimestamp(os.path.getctime(file_path))
		if timerange <= creation_time <= actual_time:
			temp_list.append((file_name, creation_time))
	
	temp_list = sorted(temp_list, key=lambda d: d[1])
	# Print the file names and their creation datetimes
	print("\n--- Temp files: ---\n")
	for file_info in temp_list:
		file_name = file_info[0]
		creation_time = file_info[1]
		print("File Name: {}".format(file_name))
		print("Creation Time: {}".format(creation_time.strftime("%Y-%m-%d %H:%M:%S")))

def check_installed_programs():
	installed_programs = []
	uninstall_key = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall"
	try:
		# Open the uninstall registry key
		with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, uninstall_key) as key:
			# Enumerate the subkeys (installed programs)
			for i in range(winreg.QueryInfoKey(key)[0]):
				subkey_name = winreg.EnumKey(key, i)
				subkey_path = rf"{uninstall_key}\{subkey_name}"
				# Open each subkey and retrieve the DisplayName value
				with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, subkey_path) as subkey:
					try:
						install_date_value = winreg.QueryValueEx(subkey, "InstallDate")[0]
						install_date = datetime.strptime(install_date_value, "%Y%m%d")
						display_name = winreg.QueryValueEx(subkey, "DisplayName")[0]
						if timerange <= install_date <= actual_time:
							installed_programs.append((display_name, install_date))
					except FileNotFoundError:
						pass
	except FileNotFoundError:
		pass
	installed_programs = sorted(installed_programs, key=lambda d: d[1])
	if installed_programs:
		print("\n--- Installed Programs: ---\n")
		for program, install_date in installed_programs:
			print("Name: {}".format(program))
			print("Install Date: {}".format(install_date))
			print("---")

def check_process():
	process_list = []
	for proc in psutil.process_iter(['pid', 'name', 'create_time']):
		try:
			create_time_formatted = datetime.fromtimestamp(proc.info['create_time']).strftime('%Y-%m-%d %H:%M:%S')
			datetime_format = datetime.strptime(create_time_formatted, '%Y-%m-%d %H:%M:%S')
			if timerange <= datetime_format <= actual_time:
				process_list.append(proc)
		except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
			pass
	process_list = sorted(process_list, key=lambda proc: proc.info['create_time'])
	if process_list:
		print("\n--- Running Processes: ---\n")
		for proc in process_list:
			create_time_formatted = datetime.fromtimestamp(proc.info['create_time']).strftime('%Y-%m-%d %H:%M:%S')
			print("Process Name: {} | PID: {} | Creation Time: {}".format(proc.info['name'], proc.info['pid'], create_time_formatted))

def retrieve_browser_history(browser_name, history_file):
	print("Browser: {}".format(browser_name))
	# Connect to the browser history database
	try:
		connection = sqlite3.connect(history_file)
	except sqlite3.OperationalError:
		print("Unable to connect to browser history database, is {} installed?".format(browser_name))
		return
	cursor = connection.cursor()
	# Execute the SQL query to retrieve the history data
	query = ""
	if browser_name == "Chrome":
		query = "SELECT url, title, last_visit_time FROM urls"
	elif browser_name == "Firefox":
		query = "SELECT url, title, last_visit_date FROM moz_places"
	elif browser_name == "Edge":
		query = "SELECT url, title, last_visit_time FROM urls"
	else:
		print("Unsupported browser")
		return
	try:
		cursor.execute(query)
	except sqlite3.OperationalError:
		print("Unable to execute query, is {} opened?".format(browser_name))
		return
	# Fetch all the rows returned by the query
	rows = cursor.fetchall()
	# Process and print the history data
	for row in rows:
		url = row[0]
		title = row[1]
		last_visit_time = None

		# Convert the last visit time from Windows epoch to Unix epoch
		if browser_name == "Chrome" or browser_name == "Edge":
			last_visit_time = int(row[2] / 1000000) - 11644473600
		elif browser_name == "Firefox":
			last_visit_time = int(row[2] / 1000000 / 1000)

		visit_datetime = datetime.fromtimestamp(last_visit_time)
		if timerange <= visit_datetime <= actual_time:
			print("URL: {}".format(url))
			print("Title: {}".format(title))
			print("Last Visit Time: {}".format(visit_datetime))
			print("---")
	# Close the database connection
	connection.close()

def check_browser():
	print("\n--- Browser History: ---\n")
	# Retrieve Chrome history
	chrome_history_file = os.path.expanduser("~") + r"\AppData\Local\Google\Chrome\User Data\Default\History"
	retrieve_browser_history("Chrome", chrome_history_file)
	# Retrieve Firefox history
	firefox_history_file = os.path.expanduser("~") + r"\AppData\Roaming\Mozilla\Firefox\Profiles"
	retrieve_browser_history("Firefox", firefox_history_file)
	# Retrieve Edge history
	edge_history_file = os.path.expanduser("~") + r"\AppData\Local\Microsoft\Edge\User Data\Default\History"
	retrieve_browser_history("Edge", edge_history_file)

def check_remote():
	# Get the network connections
	connections = psutil.net_connections(kind='inet')

	# Get the connected devices and their connection time
	connected_devices = []
	for conn in connections:
		if conn.status == psutil.CONN_ESTABLISHED:
			remote_address = conn.raddr.ip
			connect_time = datetime.now() - timedelta(seconds=conn.pid)
			if timerange <= connect_time <= actual_time:
				connected_devices.append((remote_address, connect_time))

	# Print the connected devices and their connection times
	for device in connected_devices:
		remote_address = device[0]
		connect_time = device[1].strftime("%Y-%m-%d %H:%M:%S")
		print("Remote Address: {}".format(remote_address))
		print("Connect Time: {}".format(connect_time))
		print("---")

def check_connected_devices():
	connected_devices = []
	wmi = win32com.client.GetObject("winmgmts:")
	for usb in wmi.InstancesOf("Win32_USBHub"):
		device_name = usb.DeviceID
		connect_time = usb.InstallDate
		if connect_time is not None:
			connect_time = datetime.strptime(connect_time, '%Y%m%d%H%M%S')
		if connect_time is None:
			connected_devices.append({
					'name': device_name,
					'date': connect_time})
		elif timerange <= connect_time <= actual_time:
			connected_devices.append({
					'name': device_name,
					'date': connect_time})
	connected_devices = sorted(connected_devices, key=lambda d: d['date'])
	if connected_devices:
		print("\n--- Connected Devices: ---\n")
		for device in connected_devices:
			if device['date'] is not None:
				connect_time = device['date'].strftime("%Y-%m-%d %H:%M:%S")
			print("Device Name: {}".format(device['name']))
			print("Connect Time: {}".format(connect_time))
			print("---")
	check_remote()

def check_event_logs():
	c = wmi.WMI()
	log_name = "System"
	logs = c.Win32_NTLogEvent(LogFile=log_name)
	event_logs = []
	for log in logs:
		log_time = datetime.strptime(log.TimeGenerated.split(".")[0], '%Y%m%d%H%M%S')
		event = {
			"EventID": log.EventIdentifier,
			"Timestamp": log_time,
			"Source": log.SourceName,
			"Message": log.Message
		}
		if log not in event_logs:
			if timerange <= log_time <= actual_time:
				event_logs.append(event)
	event_logs = sorted(event_logs, key=lambda d: d['Timestamp'])
	if event_logs:
		print(f"\n--- Event Logs for {log_name}: ---\n")
		for event in event_logs:
			try:
				print("Event ID: {}".format(event['EventID']))
				print("Source: {}".format(event['Source']))
				print("Timestamp: {}".format(event['Timestamp']))
				print("Message: {}".format(event['Message']))
				print("---")
			except:
				pass

def build_directory_tree(directory_path, parent_node, treeview):
	for entry in os.scandir(directory_path):
		if entry.is_dir():
			try:
				os.scandir(entry.path)
				child_node = treeview.insert(parent_node, "end", text=entry.name)
				build_directory_tree(entry.path, child_node, treeview)
			except PermissionError:
				pass

def display_directory_tree(directory_path):
	root = tk.Tk()
	root.title("Directory Tree")

	treeview = ttk.Treeview(root)
	treeview.pack(fill=tk.BOTH, expand=True)

	root_node = treeview.insert("", "end", text=directory_path)
	build_directory_tree(directory_path, root_node, treeview)

	root.mainloop()

def main():
	global timerange
	args = parse_arguments()
	if args.timerange:
		timerange = args.timerange
    if args.directorytree is None:
		display_directory_tree(os.path.expanduser("~"))
		exit()
	check_registry()
	check_recent_files()
	check_temp_files()
	check_installed_programs()
	check_process()
	check_browser()
	check_connected_devices()
	check_event_logs()

if __name__ == "__main__":
	main()
