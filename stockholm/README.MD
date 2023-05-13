# ENGLISH
## Files afected
We need to look for user root directory where is a directory called `infection`, and we need to encrypt the files inside it.

Only the files extensions affected on `Wannacry` attack need to be encrypted, we can find out all the extensions [here](https://recursos.bps.com.es/files/796/67.pdf).

All files will be renamed adding `.ft` in the end of the file, except for the files that already have `.ft` on it.
## Arguments:
Show help.
```bash
-h --help
```
Show program version.
```bash
-v --version
```
It takes the file where the key is, and decrypt all the files.
```bash
-r --reverse [key]
```
Program will print nothing.
```bash
-s --silent
```
Choose the path where the files will be decrypted.
```bash
-d --directory [path]
```
It create a directory `infection` in user root directory and take a random number to create files with file extensions affected on `Wannacry`.
```bash
-g --generate
```
## Encrypt
We will use a key with at least 16 characters and we're free to choose, in my case, I'll generate one with `Fernet` library.

## How I did it
I used function `Fernet` inside `cryptography` library to generate a random key to encrypt files, this one will save in a file called `deckey.key` in the same directory as the script.

We go through all the files inside `infection` directory looking for files extensions affected by `Wannacry` attack excluding the ones that already have `.ft` on it. Then we'll encrypt everything using `Fernet` and after that, we'll rename all files adding `.ft` in the end.

To decrypt the files, we pass `-r` as argument with the key file, then we check if the file exist to check there is no error and after that, we go through all the files to decrypt it deleting `.ft` extension.

# ESPAÑOL
## Archivos afectados
Se buscará en la carpeta raíz del usuario una carpeta llamada `infection`, y sobre ella se realizará el ataque.

Solo será efectivo contra las extensiones de archivos que fueron afectadas en su día por `Wannacry`, las podemos encontrar [aquí](https://recursos.bps.com.es/files/796/67.pdf)

Todos los archivos serán renombrados con la extensión `.ft`, si ya la tienen, no deben ser renombrados.
## Argumentos:
Muestra la ayuda.
```bash
-h --help
```
Muestra la versión de nuestro programa.
```bash
-v --version
```
Recibe la clave cifrada para poder revertir el ataque y obtener los archivos de vuelta.
```bash
-r --reverse [clave]
```
Silenciará cualquier salida por consola para no dejar rastro.
```bash
-s --silent
```
Elige la ruta donde los archivos van a ser desencriptados.
```bash
-d --directory [ruta]
```
Creará en la carpeta raíz una carpeta llamada `infection` y un número aleatorio de archivos con extensiones afectadas por `Wannacry`
```bash
-g --generate
```
## Encriptado
Utilizaremos una clave de al menos 16 caracteres y será a nuestra elección, en mi caso la generaré con ayuda de la librería Fernet.

## Realización
He utilizado la función `Fernet` dentro de la librería `cryptography` para generar una clave aleatoria con la cual encriptar los archivos, esta se guardará en un archivo llamado `deckey.key`, este se encontrará en el directorio que se ejecute nuestro programa.

Recorreremos todos los archivos dentro de la carpeta `infection` en busca de aquellos cuya extensión haya sido afectada por el ataque `Wannacry`, excluyendo todos los archivos `.ft` que encontremos. Aplicaremos un encriptado gracias a `Fernet` sobre cada archivo y además le añadiremos la extensión `.ft`.

Para desencriptar los archivos, pasaremos la flag `-r` y un archivo con la clave que desencripta, comprobaremos que existe el archivo que nos pasan para que no haya ningún error y procedemos a recorrer cada archivo, a desencriptar y eliminarles la extensión `.ft`.