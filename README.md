# TCP

## Servidor

0. Instalar Python en la máquina
1. Ejecutar el archivo [create.py](/tcp/Files/create.py) para crear los dos archivos que puede enviar el servidor TCP, y esperar a que haya creado los archivos file2.txt (250MB) y File100.zip (102MB)
2. Ejecutar el archivo [tcp_server.py](/tcp/tcp_server.py) para iniciar el servidor TCP.
> Seleccione el archivo que desea enviar al cliente, y el número de conexiones simultáneas que aceptará el servidor.

## Cliente

0. Instalar Python en la máquina
1. Ejecutar el archivo [tcp_client.py](/tcp/tcp_client.py) para iniciar el cliente TCP.
> Seleccione el número de conexiones simultáneas que se enviarán desde el cliente; debe ser igual al número de conexiones simultáneas que acepta el servidor.

## Resultados

- En el lado del servidor, se guardarán los archivos de LOG en la carpeta [LogServer](/tcp/LogServer/).

- En el lado del cliente, se guardarán los archivos de LOG en la carpeta [LogClient](/tcp/LogClient/). Además, se guardarán los archivos recibidos en la carpeta [ArchivosRecibidos](/tcp/ArchivosRecibidos/).


# UDP

## Servidor

0. Instalar Python en la máquina
1. Ejecutar el archivo [create.py](/udp/Files/create.py) para crear los dos archivos que puede enviar el servidor UDP, y esperar a que haya creado los archivos file2.txt (250MB) y File100.zip (102MB)
2. Ejecutar el archivo [udp_server.py](/udp/udp_server.py) para iniciar el servidor UDP.
> Seleccione el archivo que desea enviar al cliente.

## Cliente

0. Instalar Python en la máquina
1. Ejecutar el archivo [udp_client.py](/udp/udp_client.py) para iniciar el cliente UDP.
> Seleccione el número de conexiones simultáneas que se enviarán desde el cliente.

## Resultados

- En el lado del servidor, se guardarán los archivos de LOG en la carpeta [LogServer](/udp/LogServer/).

- En el lado del cliente, se guardarán los archivos de LOG en la carpeta [LogClient](/udp/LogClient/). Además, se guardarán los archivos recibidos en la carpeta [ArchivosRecibidos](/udp/ArchivosRecibidos/).
