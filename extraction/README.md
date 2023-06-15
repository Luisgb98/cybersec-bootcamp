Project made by [@alvgomezv](https://github.com/alvgomezv), [@cherrero42](https://github.com/cherrero42), [@jledesma](https://github.com/Falitomal) and me :D!

## Objectives
The objective of this project is to create an application that allows the user to select files to recover from the MFT (Master File Table) of a NTFS file system. Also, the appxlication allows you to read the whole disk to get all the files that you can recover and save them in a folder.

This project works in W10 and use [AnalizeMFT](https://github.com/dkovar/analyzeMFT) library to parse the MFT.

## Requisites

- You will perform a search through the whole disk.
- You will shouw a list of all recovered files.
- You will show if the file can be completely recovered, only partially or if it has been
found but its not recoverable.
- In case there are files avaliable for recover the user will be able to select wich ones
he wants to recover.

## How to use it
To use this application you need to clone this repository and inside it, clone [AnalizeMFT](https://github.com/dkovar/analyzeMFT) library. Then, run:
```bash
python3 extraction.py -h # To see the help
```
Arguments:
```bash
python3 extraction.py [DISKPATH] # To read the path disk
python3 extraction.py [DISKPATH] -t [TIME] # To read the path disk and recover the files that were deleted between [TIME] and now
python3 extraction.py [DISKPATH] -i [IMAGE] # To create an image to test the application
```

## How it works
First, we read the MFT of the disk, after that we use [AnalizeMFT](https://github.com/dkovar/analyzeMFT) to parse it. Then, we get all the files that we can recover. Then, we ask the user which files he wants to recover and we save them in a folder. All the information about the files that we can recover is saved in a file called `mft_tmp.csv` inside `analizeMFT` folder. Then we take all the info that we need about the files we want to recover as the path, the size, the name, etc.

If we want to search through the whole disk, we give you an option to do it. After the MFT is read, you can accept the search. A loading bar will appear and when it's finished, you will see all the files that can be recovered in a folder called `Recovered_deep`.