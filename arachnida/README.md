## What this project is about
This project is about [Web Scrapping](https://en.wikipedia.org/wiki/Web_scraping), in this case, we are going to extract all the images from a website and save them in a folder. This help us to learn how `http request` works and achieve a better understanding of the `html` language and web pages in general.

Second part of the project is to create a script that will check `metadata` of the images and show us the ones that we want to see.

## Mandatory part
Create a program that will download all the images from a website recursively, and save them in a folder.

Create a program that will check `metadata` of the images and show us the ones that we want to see.

The program will work with the following image formats:
- .jpg/jpeg
- .png
- .gif
- .bmp

## Arguments
Start from the given URL and follow all the links in the page recursively.
```bash
./spider -r URL
```
Start from the given URL and follow all the links in the page recursively, but only up to N levels deep. Default is 5.
```bash
./spider -r -l [N] URL
```
Start from the given URL and follow all the links in the page recursively, but save all files in PATH instead of the current directory.
```bash
./spider -p [PATH] URL
```
Check metadata of the images in the given file(s) and print the ones that match the given criteria.
```bash
./scorpion FILE [FILE2...]
```