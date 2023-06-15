# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    extraction.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lguisado <lguisado@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/06/15 13:32:51 by lguisado          #+#    #+#              #
#    Updated: 2023/06/15 15:33:19 by lguisado         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import os
import sys
import argparse
import datetime
import time
import pytsk3
from tabulate import tabulate
import psutil
from tqdm import tqdm
import pandas as pd
import subprocess
import re
import curses

magics = {
    "jpg" : [b"\xff\xd8\xff\xe0\x00\x10\x4a\x46", b"\xff\xd9"],
    "png" : [b"\x89\x50\x4e\x47\x0d\x0a\x1a\x0a", b"\x49\x45\x4e\x44\xae\x42\x60\x82"],
    "pdf" : [b"\x25\x50\x44\x46", b"\x25\x25\x45\x4f\x46"],
    "gif" : [b"\x47\x49\x46\x38", b"\x00\x3b"],
    "xml" : [b"\x50\x4b\x03\x04\x14\x00\x06\x00", b"\x50\x4b\x05\x06"],
}

good_recovered_files = []
recoverable = {}
selected_files = {}
disk = 0

analyzeMFT_path = "./analyzeMFT/analyzeMFT.py"
mft_file_path = "./analyzeMFT/mft_tmp"
mft_parse_file_path = "./analyzeMFT/mft_tmp.csv"

def create_image_from_disk(disk_path, image_path):
    disk = rf"\\.\\{disk_path}"
    img_info = pytsk3.Img_Info(disk)
    with open(image_path, "wb") as output_file:
        offset = 0
        chunk_size = 1024 * 1024
        while offset < img_info.get_size():
            data = img_info.read(offset, chunk_size)
            output_file.write(data)
            offset += chunk_size
    print(f"Image {image_path} created successfully")

def print_directory_table(directory):
    table = [["Name", "Type", "Size", "Create Date", "Modify Date"]]
    for f in directory:
        name = f.info.name.name
        if f.info.meta.type == pytsk3.TSK_FS_META_TYPE_DIR:
            f_type = "DIR"
        else:
            f_type = "FILE"
        size = f.info.meta.size
        create = f.info.meta.crtime
        modify = f.info.meta.mtime
        table.append([name, f_type, size, create, modify])
    print(tabulate(table, headers="firstrow"))

def ft_read_disk(disk):
    '''Read disk'''
    image = pytsk3.Img_Info(disk)
    try:
        partitionTable = pytsk3.Volume_Info(image)
    except Exception as error:
        print(error)
        exit(1)
    try:
        fileSystemObject = pytsk3.FS_Info(image, offset=partitionTable[0].start*512)
    except Exception as error:
        print(error)
        exit(1)
    return fileSystemObject

def ft_parse_MFT(mft_file_path):
    command = ["python3", analyzeMFT_path, "-f", mft_file_path,  "-o", mft_parse_file_path]
    subprocess.run(command)

def ft_check_MFT(mft_parse_file_path):
    df = pd.read_csv(mft_parse_file_path, encoding="latin-1")

    for index, row in df.iterrows():
        good_value = row['Good']
        record_type = row['Record type']
        filename = row['Filename']
        modif_date = row['Std Info Access date']
        filename1 = row['Filename #1']
        active_value = row['Active']
        if good_value == 'Good' and record_type == 'File' and active_value == "Inactive":
            if "Zone.Identifier" not in filename1:
                good_recovered_files.append([filename1, modif_date])
            sequence_number = row['Sequence Number']
            parent_file_rec = row['Parent File Rec. #']

def ft_extract_MFT(file):
    content = file.read_random(0, file.info.meta.size)
    with open(mft_file_path, 'wb') as output:
        output.write(content)

def search_deleted_files(disk_path):
    disk = rf"\\.\\{disk_path}"
    try:
        img_info = pytsk3.Img_Info(disk)
        fs_info = pytsk3.FS_Info(img_info)
        mft_file = fs_info.open("/$MFT")
    except:
        print("Disk not found")
        sys.exit()
    ft_extract_MFT(mft_file)
    ft_parse_MFT(mft_file_path)
    ft_check_MFT(mft_parse_file_path)

def deep_search(disk_path):
    total = None
    for disk in psutil.disk_partitions():
        if disk_path in disk.device or disk_path in disk.mountpoint:
            total = psutil.disk_usage(disk.mountpoint).total
    if total is None:
        print("Error: Disk not found")
        sys.exit()
    size = 512
    blocks = total/size
    count = 0
    offset = 0
    with tqdm(total=blocks, unit='block') as progress_bar:
        try:
            d = open(f"\\\\.\\\\{disk_path}", "rb")
        except:
            print("Disk cannot be read, format must be: \\\\.\\\\D:")
            sys.exit()
        else:
            bytes = d.read(size)
            progress_bar.update(1)
            try:
                while bytes:
                    for key, value in magics.items():
                        found = bytes.find(value[0])
                        if found >= 0:
                            drec = True
                            if not os.path.exists(".\\Recovered_deep"):
                                os.makedirs(".\\Recovered_deep")     
                            with open(f".\\Recovered_deep\\{str(count)}.{key}", "wb") as f:
                                f.write(bytes[found:])
                                while drec is True:
                                    bytes = d.read(size)
                                    found = bytes.find(value[1])
                                    if found >= 0:
                                        f.write(bytes[:found+2])
                                        d.seek((offset+1)*size)
                                        drec = False
                                        count += 1
                                    else:
                                        f.write(bytes)
                    bytes = d.read(size)
                    progress_bar.update(1)
                    offset += 1
                d.close()
                print(f"\nRecovered {count} files in the deep search")
            except KeyboardInterrupt:
                progress_bar.close()
                print("Program stopped!")
                sys.exit()

def get_from_disk(disk_path, selected_files):
    total = None
    for disks in psutil.disk_partitions():
        if disk_path in disks.device or disk_path in disks.mountpoint:
            total = psutil.disk_usage(disks.mountpoint).total
    if total is None:
        print("Error: Disk not found")
        sys.exit()
    if not os.path.exists(".\\Recovered_mft"):
            os.makedirs(".\\Recovered_mft")
    for key, value in selected_files.items():
        with open(rf"\\.\\{disk_path}", "rb") as d:
            bytes = d.read(value["offset"] + value["file_size"])
            with open(f".\\Recovered_mft\\{key}", "wb") as f:
                f.write(bytes[value["offset"]:])

def get_file_attributes(disk_path, timelaps):
    disk = rf"\\.\\{disk_path}"
    img_info = pytsk3.Img_Info(disk)
    fs_info = pytsk3.FS_Info(img_info)
    for file in good_recovered_files:
        try:
            unix_date = datetime.datetime.strptime(file[1], "%Y-%m-%d %H:%M:%S.%f").timestamp()
        except ValueError:
            unix_date = datetime.datetime.strptime(file[1], "%Y-%m-%d %H:%M:%S").timestamp()
        if unix_date >= timelaps:
            mft_file = fs_info.open(file[0])
            for attribute in mft_file:
                if attribute.info.type == pytsk3.TSK_FS_ATTR_TYPE_NTFS_DATA and attribute.info.name != b'Zone.Identifier':
                    for run in attribute:
                        cluster_start = run.addr * fs_info.info.block_size
                        cluster_length = run.len * fs_info.info.block_size
                        recoverable[file[0].lstrip('/')] = {
                            "offset" : cluster_start, 
                            "file_size" : attribute.info.size, 
                            "cluster_size" : cluster_length,
                            "access_date" : file[1]}

def select_options(stdscr):
    stdscr.clear()

    selected_options = set()
    current_option = 0

    while True:
        stdscr.clear()
        intro_message = "Select files to recover:"
        stdscr.addstr(0, 0, intro_message, curses.A_BOLD)

        for i, (name, data) in enumerate(recoverable.items()):
            if i == current_option:
                stdscr.addstr(i+1, 0, "> " + f"{name:35s}" + " <" + f" | size: {float(data['file_size']/1024):.2f}KB".ljust(20) +f"| access date: {data['access_date']}", curses.A_REVERSE)
            elif i in selected_options:
                stdscr.addstr(i+1, 0,"* " + f"{name:35s}" + 2*" "+ f" | size: {float(data['file_size']/1024):.2f}KB".ljust(20) + f"| access date: {data['access_date']}")
            else:
                stdscr.addstr(i+1, 0, f"{name:35s}" + 4*" " + f" | size: {float(data['file_size']/1024):.2f}KB".ljust(20) + f"| access date: {data['access_date']}")

        start_option = "Start"
        if current_option == len(recoverable):
            stdscr.addstr(len(recoverable)+1, 0, "> " + start_option + " <", curses.A_REVERSE)
        else:
            stdscr.addstr(len(recoverable)+1, 0, start_option)

        stdscr.refresh()

        try:
            key = stdscr.getch()
        except KeyboardInterrupt:
            print("Program stopped!")
            sys.exit()

        if key == curses.KEY_UP:
            current_option = (current_option - 1) % (len(recoverable) + 1)
        elif key == curses.KEY_DOWN:
            current_option = (current_option + 1) % (len(recoverable) + 1)
        elif key == ord('\n'):
            if current_option == len(recoverable):
                break
            else:
                if current_option in selected_options:
                    selected_options.remove(current_option)
                else:
                    selected_options.add(current_option)

    if len(selected_options) > 0:
        print("Recovered files:")
        for option_idx in selected_options:
            option_name = list(recoverable.keys())[option_idx]
            print(option_name)
        remove = []
        for i in range(len(recoverable)):
            if i not in selected_options:
                remove.append(i)
        items = list(recoverable.items())
        filtered_items = [item for i, item in enumerate(items, start=0) if i not in remove]
        selected_files = dict(filtered_items)
        get_from_disk(disk, selected_files)

def parse_arguments():
    parser = argparse.ArgumentParser(description="Tool for recovering recently deleted files on NTFS")
    parser.add_argument("disk", help="Path to the disk")
    parser.add_argument("-i", "--image", action="store", help="Create an image from a disk file")
    parser.add_argument("-t", "--timelaps", action="store", help="Time range in hours, default 24h" )
    arg = parser.parse_args()
    if arg.disk is None:
        print("A disk must be provided")
        sys.exit()
    if re.match(r'^[A-Z]:$', arg.disk) is None:
        print("Disk format must be uppercase letter followed by a colon (ex: 'D:')")
        sys.exit()
    try:
        date_format = "%d-%m-%Y"
        if arg.timelaps is not None:
            arg.timelaps = datetime.datetime.strptime(arg.timelaps, date_format).timestamp()
        else:
            arg.timelaps = time.time() - (24 * 60 * 60)
        return arg
    except Exception as e:
        print(f"Error: {e}")
        sys.exit()

if __name__ == "__main__":
    arg = parse_arguments()
    disk = arg.disk
    if arg.image:
        create_image_from_disk(arg.disk, arg.image)
    search_deleted_files(arg.disk)
    get_file_attributes(arg.disk, arg.timelaps)
    curses.wrapper(select_options)
    print("Do you want to do a deep search though the whole disk? [Y/N]")
    key = input()
    if key in ["y", "Y", "YES", "yes"]:
        deep_search(arg.disk)