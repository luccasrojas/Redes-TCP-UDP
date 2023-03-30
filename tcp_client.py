import socket
import hashlib
import os
import time
import threading

# Configuración del servidor
IP = socket.gethostbyname(socket.gethostname())
PORT = 4456
ADDR = (IP, PORT)
SIZE = 4096
FORMAT = "utf-8"

# Configuración del directorio para almacenar archivos recibidos
RECEIVED_DIR = './ArchivosRecibidos'

# Función para recibir archivo del servidor
def recibir_archivo(num_cliente):
    # Crear socket para conectarse con el servidor
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((IP, PORT))
        print(f"Conexión establecida con el servidor para el cliente {num_cliente}.")
        # Enviar mensaje de confirmación de recepción
        print("Mandando peticion para conectar")
        client_socket.sendall(b"Listo para conectar")
        print("Ack listo para conectar")
        #ACK
        client_socket.recv(SIZE)
        print("Conectado y listo para recibir")
        
        # Abrir archivo para escritura
        
        counter = 0
        with open(os.path.join(RECEIVED_DIR, f"Cliente{num_cliente}.txt"), 'wb') as f:
            while True:
                data = client_socket.recv(SIZE)
                client_socket.sendall(b"ACK")
                if data == b"FIN":
                    break
                f.write(data)
                counter += 1

        print(counter)
        print("El tamanio del archivo es de", os.path.getsize(os.path.join(RECEIVED_DIR, f"Cliente{num_cliente}.txt")), "bytes")

        #ACK llego el archivo
        client_socket.sendall(b"Archivo recibido")

        hash_value = client_socket.recv(SIZE).decode()
        print(f"Archivo recibido para el cliente {num_cliente}.")
        # Calcular hash del archivo recibido y comparar con el valor enviado por el servidor
        with open(os.path.join(RECEIVED_DIR, f"Cliente{num_cliente}.txt"), 'rb') as f:
            md5 = hashlib.md5()
            for chunk in iter(lambda: f.read(4096), b""):
                md5.update(chunk)
            file_hash =md5.hexdigest()
        
        print(hash_value)
        print(file_hash)
        if file_hash == hash_value:
            print(f"El archivo recibido para el cliente {num_cliente} es válido.")
        else:
            print(f"El archivo recibido para el cliente {num_cliente} es inválido.")

        # Enviar mensaje de confirmación de recepción
        client_socket.sendall(b"Me llego el archivo y el hash")
    except:
        print(f"No se pudo establecer conexión con el servidor para el cliente {num_cliente}.")
    finally:
        # Cerrar socket
        client_socket.close()
num_clientes = int(input("Ingrese el numero de clientes: "))
for i in range(1, num_clientes+1):
    thread = threading.Thread(target=recibir_archivo, args=(i,))
    thread.start()
