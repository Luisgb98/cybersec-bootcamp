## What this script does?
A program that extracts the following artifacts on a given time lapse. If the user doesn't give your program a time range it should fall back to a default value, for ex: last 24h, last week, last month...

## Artifacts
- Registry branches changes date (CurrentVersionRun).
- Recent used/opened files.
- Temporary files.
- Installed programs.
- Processes on execution.
- Web browser history.
- Connected devices.
- Events logs.

## Bonus part
- Show the directory tree on some kind of graphic view. 

## How it works?
The program will receive the time range in the following format: `YYYY-MM-DD` or `DD-MM-YYYY`. The program will receive the time range as an argument with the help of a flag `-t`, if the user doesn't give your program a time range it should fall back to a default value, in this case, the default value is the last 24h.
```bash
python3 recovery.py -t YYYY-MM-DD or DD-MM-YYYY
```

## Validate input dates
To validate the input date, I used `datetime` library to check if the date is valid or not. If the date is not valid, the program will exit with an error message.

## Registry branches changes date (CurrentVersionRun)
To get the registry branches changes date, I used library called `winreg` to access the registry and get the last modified date of the registry key. `CurrentVersionRun` is located in `SOFTWARE\Microsoft\Windows\CurrentVersion\Run`. To get the last modified date, I used `winreg.OpenKey` to open the registry key and `winreg.QueryInfoKey` to get the last modified date, that's give us a non readable date, so I used `datetime` library and `epoch` time to convert the date to a readable format.

## Recent used/opened files
To get recent used/opened files, we go to the path `C:\Users\%username%\AppData\Roaming\Microsoft\Windows\Recent` and get all `.lnk` extension files, these files are shortcuts to the original file that indicate the last time the file was opened. I used `os.path.expanduser` to get the username of the current user, and `os.listdir` to get all files in the directory.

## Temporary files
To get temporary files, we go to the path I used `tempfile` library to get the temporary directory path, and `os.listdir` to get all files in the directory.

## Installed programs
To get installed programs, we go to the path `SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall`, then I got all `subkeys` in the path, and get the `DisplayName` and `InstallDate` of each subkey. To get the `InstallDate`, I used `winreg.QueryValueEx` and `winreg.QueryValueEx` to get the `DisplayName`.

## Processes on execution
To get processes on execution, I used `psutil` library to get all running processes, and `psutil.Process` to get the process name and the process start time. In my case I iterate over `pid`, `name` and `create_time` to get the information.

## Web browser history
To get web browser history, I used `sqlite3` library to access the database of the web browser. In my case I iterate over `url`, `title`, `last_visit` and to get all the information. I support the following web browsers:
- Google Chrome
- Mozilla Firefox
- Microsoft Edge

## Connected devices
To get connected devices, I used `wmi` library to get all connected devices. In my case I iterate over `DeviceID`and `InstallDate` to get all the information. And I used `psutil` library to get remote connections. In my case I iterate over `raddr.ip` and `conn.pid`, I used `conn.pid` and `timedelta` to get the connection start time.

## Events logs
To get events logs, I used `win32evtlog` library to get all events logs. In my case I iterate over `System` logs to get `EventIdentifier`. `TimeGenerated`, `SourceName` and `Message` information.

## Directory tree graphic view
I used `tkinter` to create a GUI and `os.scandir` to get the directory tree. A graphical representation of the directory tree is shown below with a loop to get all subdirectories and files.