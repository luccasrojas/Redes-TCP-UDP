import socket
import os
import time
import threading
import queue 

# Configuración del servidor
IP = "127.0.0.1" # "192.168.1.142"
PORT = 10000
ADDR = (IP, PORT)
SIZE = 4096
FORMAT = "utf-8"

# Configuración del directorio para almacenar archivos recibidos
RECEIVED_DIR = './ArchivosRecibidos'

# Función para recibir archivo del servidor
def recibir_archivo(num_cliente):
    # Crear socket para conectarse con el servidor
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.settimeout(3)  # Establecer timeout de 3 segundos
    
    try:
        client_socket.connect((IP, PORT))
        print(f"Conexión establecida con el servidor para el cliente {num_cliente}.")
        # Enviar mensaje de confirmación de recepción
        print("Mandando peticion para conectar")
        client_socket.sendto(b"Listo para conectar", ADDR)

        # Abrir archivo para escritura        
        counter = 0
        t1 = time.time()
        with open(os.path.join(RECEIVED_DIR, f"Cliente{num_cliente}.txt"), 'wb') as f:
            while True:
                try:
                    data, addr = client_socket.recvfrom(SIZE)
                except socket.timeout:
                    print(f"Timeout al recibir datos del servidor para el cliente {num_cliente}.")
                    break  # Salir del while True si se excede el timeout

                if data == b"FIN":
                    break
                f.write(data)
                counter += 1
        print(counter)
        t2 = time.time()

        print(f"Archivo recibido para el cliente {num_cliente}.")
    except:
        print(f"Error al recibir el archivo para el cliente {num_cliente}.")
    finally:

        log_file_name = time.strftime("%Y-%m-%d-%H-%M-%S-log.txt")
        log_file_path = os.path.join("./LogClient", log_file_name)
        file_size = os.path.getsize(os.path.join(RECEIVED_DIR, f"Cliente{num_cliente}.txt"))
        tiempo = t2-t1
        with open(log_file_path, "a") as f:
            f.write(f"Cliente: {num_cliente}, NombreArchivo: Cliente{num_cliente}.txt, TamanioArchivo: {file_size}, " 
                    f"Tiempo: {tiempo}\n")

        # Cerrar socket
        client_socket.close()

if __name__ == "__main__":
    num_clientes = int(input("Ingrese el número de clientes: "))
    for i in range(1, num_clientes+1):
        thread = threading.Thread(target=recibir_archivo, args=(i,))
        thread.start()
