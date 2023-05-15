Para crear e iniciar el contenedor `ft_onion` con la imagen de debian.
```bash
$>docker run -it -p 4242:4242 -p 80:80 --name ft_onion debian
```
Para iniciar nuestro container.
```bash
$>docker start -i ft_onion
```
Actualizamos todos los paquetes.
```bash
$>apt update
```
Instalamos un editor de texto.
```bash
$>apt install vim
```
Instalamos los paquetes necesarios para el `ft_onion`.

Paquete para configurar nuestro servidor.
```bash
$>apt install nginx
```
Creamos en el directorio `/var/www/` una carpeta con el nombre `lguisado`(en mi caso), para guardar nuestro `html/css`.

Nos movemos a `/etc/nginx/` para configurar nuestro servidor.

Vamos a la carpeta `sites-available` y creamos una archivo `lguisado`(en mi caso), para guardar nuestra config.

Añadimos el siguiente codigo:
```bash
server {
	listen 80;
	root /var/www/lguisado;
	index index.html;
	server_name lguisado www.lguisado;
	location / {
		try_files $uri $uri/ =404;
	}
}
```
Hacemos un symbolic link en `sites-enabled`, para que `nginx` sepa que tiene que abrirlo.
```bash
$>ln -s /etc/nginx/sites-available/lguisado /etc/nginx/sites-enabled/lguisado
```
Reiniciamos el servicio de `nginx` y empezaría a funcionar.

Paquete para configurar el `ssh` para poder conectarnos.
```bash
$>apt install openssh-server
```
Nos movemos a `/etc/ssh/` para poder cambiar la configuracion de nuestro `ssh` en `sshd_config`.

Descomentamos la opcion de puerto y activamos el puerto `4242`.

Descomentamos la opcion de `PermitRootLogin` y le ponemos `yes` para poder conectarnos como root.

Reiniciamos el servicio `ssh`.
```bash
$>service ssh restart
```
Paquete necesario para crear la web `.onion`.
```bash
$>apt install tor
```
Nos movemos a `/etc/tor` y editamos el archivo `torrc`.

Descomentamos las opciones de `HiddenServiceDir` y `HiddenServicePort` para que `tor` pueda redirigir los datos de `nginx`.

Reiniciamos el servicio de `tor`.
```bash
$>service tor restart
```
Nos movemos a `/var/lib/tor/hidden_service` y hacemos un cat del hostname para tener nuestro `.onion`.

Ponemos nuestro `.onion` en nuestro navegador tor y ya estariamos dentro.

Instalamos `sudo` para poder poner password.

Creamos un usuario y le añadimos la ssh desde la consola normal con:
```bash
$> ssh-copy-id user@localhost -p 4242
```
Ahora podemos iniciar sesión ya que nuestra `key` esta guardada.

Informacion extraida de:
- [NGINX](https://jgefroh.medium.com/a-guide-to-using-nginx-for-static-websites-d96a9d034940)
- [SSH](https://linuxhint.com/enable-ssh-server-debian/)
- [TOR](https://community.torproject.org/relay/setup/bridge/debian-ubuntu/)