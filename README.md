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

# Tabla de resultados de pruebas

Esta tabla muestra los resultados de las pruebas realizadas en el laboratorio, con el fin de comparar los tiempos de transferencia de archivos de diferentes tamaños, utilizando TCP y UDP.

## Pruebas TCP

### Prueba 1
1 cliente, archivo de 101.96MB

| # | Entrega exitosa | Puerto Cliente | Puerto Servidor | Bytes Cliente (MB) | Bytes Servidor (MB) | Tasa Cliente (MBps) | Tasa Servidor (MBps) | Tiempo Cliente (ms) | Tiempo Servidor (ms) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | True | 58308 | 4456 | 101.96 | 101.96 | 174.23 | 174.23 | 585.22 | 585.22 |

### Prueba 2
1 cliente, archivo de 250MB

| # | Entrega exitosa | Puerto Cliente | Puerto Servidor | Bytes Cliente (MB) | Bytes Servidor (MB) | Tasa Cliente (MBps) | Tasa Servidor (MBps) | Tiempo Cliente (ms) | Tiempo Servidor (ms) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | True | 58488 | 4456 | 250.00 | 250.00 | 138.56 | 139.39 | 1804.33 | 1793.48 |

### Prueba 3
5 clientes, archivo de 101.96MB

| # | Entrega exitosa | Puerto Cliente | Puerto Servidor | Bytes Cliente (MB) | Bytes Servidor (MB) | Tasa Cliente (MBps) | Tasa Servidor (MBps) | Tiempo Cliente (ms) | Tiempo Servidor (ms) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 3 | True | 58502 | 4456 | 101.96 | 101.96 | 51.00 | 51.05 | 1999.38 | 1997.30 |
| 2 | True | 58501 | 4456 | 101.96 | 101.96 | 49.80 | 49.85 | 2047.62 | 2045.54 |
| 1 | True | 58500 | 4456 | 101.96 | 101.96 | 50.36 | 50.41 | 2024.82 | 2022.74 |
| 4 | True | 58503 | 4456 | 101.96 | 101.96 | 48.93 | 48.96 | 2083.73 | 2082.64 |
| 5 | True | 58504 | 4456 | 101.96 | 101.96 | 49.63 | 49.64 | 2054.63 | 2054.06 |

### Prueba 4
5 clientes, archivo de 250MB

| # | Entrega exitosa | Puerto Cliente | Puerto Servidor | Bytes Cliente (MB) | Bytes Servidor (MB) | Tasa Cliente (MBps) | Tasa Servidor (MBps) | Tiempo Cliente (ms) | Tiempo Servidor (ms) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | True | 58617 | 4456 | 250.00 | 250.00 | 57.53 | 57.55 | 4345.83 | 4344.32 |
| 4 | True | 58619 | 4456 | 250.00 | 250.00 | 56.41 | 56.43 | 4431.48 | 4430.47 |
| 1 | True | 58616 | 4456 | 250.00 | 250.00 | 54.32 | 54.35 | 4602.31 | 4599.80 |
| 3 | True | 58618 | 4456 | 250.00 | 250.00 | 54.57 | 54.59 | 4581.19 | 4579.68 |
| 5 | True | 58620 | 4456 | 250.00 | 250.00 | 54.25 | 54.25 | 4608.06 | 4608.06 |

### Prueba 5
10 clientes, archivo de 101.96MB

| # | Entrega exitosa | Puerto Cliente | Puerto Servidor | Bytes Cliente (MB) | Bytes Servidor (MB) | Tasa Cliente (MBps) | Tasa Servidor (MBps) | Tiempo Cliente (ms) | Tiempo Servidor (ms) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | True | 58646 | 4456 | 101.96 | 101.96 | 24.81 | 24.81 | 4110.42 | 4109.42 |
| 1 | True | 58637 | 4456 | 101.96 | 101.96 | 24.81 | 24.83 | 4110.49 | 4106.41 |
| 8 | True | 58644 | 4456 | 101.96 | 101.96 | 24.20 | 24.22 | 4213.02 | 4210.02 |
| 9 | True | 58645 | 4456 | 101.96 | 101.96 | 24.07 | 24.08 | 4236.60 | 4233.60 |
| 2 | True | 58638 | 4456 | 101.96 | 101.96 | 24.07 | 24.09 | 4236.67 | 4232.60 |
| 3 | True | 58639 | 4456 | 101.96 | 101.96 | 23.93 | 23.95 | 4261.31 | 4258.24 |
| 4 | True | 58640 | 4456 | 101.96 | 101.96 | 23.91 | 23.93 | 4264.86 | 4261.78 |
| 6 | True | 58642 | 4456 | 101.96 | 101.96 | 24.87 | 24.89 | 4100.26 | 4097.19 |
| 7 | True | 58643 | 4456 | 101.96 | 101.96 | 25.45 | 25.46 | 4006.11 | 4004.22 |
| 5 | True | 58641 | 4456 | 101.96 | 101.96 | 24.41 | 24.43 | 4177.98 | 4173.90 |

### Prueba 6
10 clientes, archivo de 250MB

| # | Entrega exitosa | Puerto Cliente | Puerto Servidor | Bytes Cliente (MB) | Bytes Servidor (MB) | Tasa Cliente (MBps) | Tasa Servidor (MBps) | Tiempo Cliente (ms) | Tiempo Servidor (ms) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | True | 58648 | 4456 | 250.00 | 250.00 | 25.22 | 25.22 | 9913.87 | 9911.60 |
| 2 | True | 58649 | 4456 | 250.00 | 250.00 | 24.79 | 24.80 | 10086.64 | 10081.37 |
| 6 | True | 58653 | 4456 | 250.00 | 250.00 | 24.80 | 24.81 | 10081.37 | 10078.37 |
| 3 | True | 58650 | 4456 | 250.00 | 250.00 | 24.56 | 24.57 | 10179.88 | 10176.61 |
| 4 | True | 58651 | 4456 | 250.00 | 250.00 | 24.49 | 24.49 | 10210.19 | 10208.19 |
| 0 | True | 58657 | 4456 | 250.00 | 250.00 | 24.23 | 24.23 | 10319.16 | 10318.16 |
| 5 | True | 58652 | 4456 | 250.00 | 250.00 | 24.18 | 24.18 | 10340.91 | 10338.92 |
| 9 | True | 58656 | 4456 | 250.00 | 250.00 | 24.47 | 24.47 | 10217.73 | 10216.73 |
| 8 | True | 58655 | 4456 | 250.00 | 250.00 | 24.48 | 24.49 | 10211.19 | 10209.20 |
| 7 | True | 58654 | 4456 | 250.00 | 250.00 | 24.42 | 24.42 | 10237.28 | 10236.28 |

<br>

## Pruebas UDP

### Prueba 1
1 cliente, archivo de 101.96MB

| # | Puerto Cliente | Puerto Servidor | Bytes Cliente (MB) | Bytes Servidor (MB) | Tasa Cliente (MBps) | Tasa Servidor (MBps) | Tiempo Cliente (ms) | Tiempo Servidor (ms) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 52564 | 10000 | 87.80 | 101.96 | 245.96 | 288.05 | 356.98 | 353.98 |

### Prueba 2
1 cliente, archivo de 250MB

| # | Puerto Cliente | Puerto Servidor | Bytes Cliente (MB) | Bytes Servidor (MB) | Tasa Cliente (MBps) | Tasa Servidor (MBps) | Tiempo Cliente (ms) | Tiempo Servidor (ms) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 59306 | 10000 | 218.70 | 250.00 | 268.64 | 308.41 | 814.12 | 810.60 |

### Prueba 3
5 clientes, archivo de 101.96MB

| # | Puerto Cliente | Puerto Servidor | Bytes Cliente (MB) | Bytes Servidor (MB) | Tasa Cliente (MBps) | Tasa Servidor (MBps) | Tiempo Cliente (ms) | Tiempo Servidor (ms) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 3 | 61108 | 10000 | 69.48 | 101.96 | 35.69 | 52.48 | 1946.98 | 1942.83 |
| 2 | 61107 | 10000 | 71.81 | 101.96 | 36.56 | 51.91 | 1964.09 | 1964.09 |
| 1 | 61106 | 10000 | 69.08 | 101.96 | 35.30 | 52.15 | 1957.06 | 1955.07 |
| 4 | 61109 | 10000 | 70.84 | 101.96 | 36.37 | 52.45 | 1947.98 | 1943.92 |
| 5 | 61110 | 10000 | 71.23 | 101.96 | 36.38 | 52.13 | 1958.09 | 1956.03 |

### Prueba 4
5 clientes, archivo de 250MB

| # | Puerto Cliente | Puerto Servidor | Bytes Cliente (MB) | Bytes Servidor (MB) | Tasa Cliente (MBps) | Tasa Servidor (MBps) | Tiempo Cliente (ms) | Tiempo Servidor (ms) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | 58308 | 10000 | 173.48 | 250.00 | 35.97 | 51.85 | 4823.04 | 4822.04 |
| 4 | 58310 | 10000 | 174.33 | 250.00 | 36.17 | 51.88 | 4820.03 | 4819.03 |
| 1 | 58307 | 10000 | 172.87 | 250.00 | 35.73 | 51.68 | 4838.12 | 4837.15 |
| 3 | 58309 | 10000 | 171.27 | 250.00 | 35.38 | 51.67 | 4840.17 | 4838.14 |
| 5 | 58311 | 10000 | 178.29 | 250.00 | 36.84 | 51.66 | 4840.19 | 4839.19 |

### Prueba 5
10 clientes, archivo de 101.96MB

| # | Puerto Cliente | Puerto Servidor | Bytes Cliente (MB) | Bytes Servidor (MB) | Tasa Cliente (MBps) | Tasa Servidor (MBps) | Tiempo Cliente (ms) | Tiempo Servidor (ms) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 51694 | 10000 | 69.13 | 101.96 | 16.76 | 24.77 | 4124.43 | 4116.91 |
| 1 | 51685 | 10000 | 68.53 | 101.96 | 16.68 | 24.85 | 4107.32 | 4102.79 |
| 8 | 51691 | 10000 | 70.04 | 101.96 | 16.88 | 24.60 | 4149.83 | 4144.76 |
| 9 | 51693 | 10000 | 69.27 | 101.96 | 16.84 | 24.86 | 4112.37 | 4102.24 |
| 2 | 51686 | 10000 | 69.97 | 101.96 | 16.93 | 24.69 | 4132.47 | 4129.95 |
| 3 | 51687 | 10000 | 68.83 | 101.96 | 16.73 | 24.79 | 4114.37 | 4112.37 |
| 4 | 51688 | 10000 | 68.49 | 101.96 | 16.76 | 24.99 | 4085.51 | 4079.51 |
| 6 | 51690 | 10000 | 68.42 | 101.96 | 16.58 | 24.73 | 4126.94 | 4122.92 |
| 7 | 51692 | 10000 | 68.15 | 101.96 | 16.56 | 24.82 | 4115.37 | 4108.86 |
| 5 | 51689 | 10000 | 70.66 | 101.96 | 17.02 | 24.59 | 4151.90 | 4146.82 |

### Prueba 6
10 clientes, archivo de 250MB

| # | Puerto Cliente | Puerto Servidor | Bytes Cliente (MB) | Bytes Servidor (MB) | Tasa Cliente (MBps) | Tasa Servidor (MBps) | Tiempo Cliente (ms) | Tiempo Servidor (ms) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 50680 | 10000 | 166.33 | 250.00 | 16.23 | 24.41 | 10245.89 | 10242.86 |
| 2 | 50681 | 10000 | 168.87 | 250.00 | 16.46 | 24.38 | 10256.24 | 10253.73 |
| 6 | 50685 | 10000 | 167.39 | 250.00 | 16.34 | 24.42 | 10246.69 | 10238.29 |
| 3 | 50682 | 10000 | 166.03 | 250.00 | 16.28 | 24.52 | 10199.49 | 10195.40 |
| 4 | 50683 | 10000 | 167.35 | 250.00 | 16.31 | 24.38 | 10257.25 | 10253.21 |
| 0 | 50689 | 10000 | 167.24 | 250.00 | 16.30 | 24.38 | 10258.75 | 10252.69 |
| 5 | 50684 | 10000 | 168.17 | 250.00 | 16.39 | 24.37 | 10260.27 | 10259.21 |
| 9 | 50688 | 10000 | 168.37 | 250.00 | 16.41 | 24.38 | 10259.74 | 10254.71 |
| 8 | 50687 | 10000 | 165.74 | 250.00 | 12.51 | 24.42 | 13245.86 | 10237.62 |
| 7 | 50686 | 10000 | 167.24 | 250.00 | 16.31 | 24.40 | 10251.20 | 10246.15 |




