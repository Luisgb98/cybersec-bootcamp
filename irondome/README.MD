## Requisites
- Program needs to be execute as daemon service.
- Only root user can execute it.
- First argument set the route where the script will monitor
- Others argument will set specific extensions to monitor, if not provided, all extensions will be monitored.
- It can't superate 100MB of memory use.

## What this script does?
This script will detect:
- Disk read abuse.
- Intensive use of cryptography service.
- Entropy change of files.
- All alerts will be saved at /var/logs/irondome/irondome.log.

## Disk read abuse
To check if there's a disk read abuse, we'll use `watchdog` library to check disk stats. `Observer` from `watchdog` check the directory finding if there're some movements, using `events`, we create a class that handle `disk read`, we'll choice `on_created`, `on_deleted` and `on_modified`. Then we made a count each 10 seconds, if we get a high amount of `disk read events`, then we'll raise a warning.

## Intensive use of cryptographic activity
I tried my own `stockholm` proyect that uses `Fernet` to get a process that goes up but there's no process that matches `Fernet` or other library, it always shows `python3`, so what I did was check `cpu percent` to see if there's an anomaly. To do this, I used `psutil` library, I get the `cpu percent`, if it's higher than a percent I want, then I'll raise a warning.

## Changes in the entropy of the files
To check if there's a change in the entropy of the files, I used an algorithm that I found on [stackoverflow](https://stackoverflow.com/questions/990477/how-to-calculate-the-entropy-of-a-file). This algorithm will calculate the entropy of a file, so I got an initial entropy and then I'll check if there's a change in the entropy, if there's a change, then I'll raise a warning.

## Creating backups
To create a backup of the files, I used `shutil` library to copy the tree of the directory to another directory. To do it periodically, I used `threading` library to create a thread that will execute the backup function each `x` seconds that I want.

I also did the bonus part, incremental backups, to do it, I used `watchdog` library to check if there's a change in the directory, if there's a change, then I'll execute a backup function that will copy the file that was modified to another directory using `shutil` library.

## Checking Root and Linux
To check if the user is running the service as `root` and if the OS is `Linux`, I used `os` library to get the user and the OS, then I'll check if the user is `root` and if the OS is `Linux`, if not, then I'll raise a warning.

## Demo mode
To test my irondome, I added a flag `-g` that will run the script in demo mode, this mode will create a directory with a lot of files.