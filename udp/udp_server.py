import socket
import threading
import os
import hashlib
import time

IP = "0.0.0.0"
PORT = 10000
ADDR = (IP, PORT)
SIZE = 4096
FORMAT = "utf-8"

# Directorio donde se encuentran los archivos
FILE_DIR = "./Files"

# Archivos disponibles para envío
FILES = {
    "file1": "File100.zip",
    "file2": "file2.txt"
}

def handle_client(conn, addr, file_name):
    #Establecer la conexion con el cliente
    print(f"[SERVER] Cliente conectado desde {addr}")

    """ Receiving the filename and filesize from the client. """
    
    # Abrir archivo y enviar datos
    file_path = os.path.join(FILE_DIR, file_name)
    file_size = os.path.getsize(file_path)

    print("Enviando archivo de tamaño", file_size, "bytes")
    counter = 0
    with open(file_path, "rb") as f:
        t1 = time.time()
        while True:
            # Enviar datos del tamaño del buffer hasta que se acaben
            data = f.read(SIZE)
            if not data:
                break
            conn.sendto(data, addr)
            counter += 1
    print(counter)
    conn.sendto(b"FIN", addr)
        
    print("Archivo enviado")
    
    t2 = time.time()
    tiempo = t2 - t1
    
    # Registro de la conexión en el archivo de logs
    log_file_name = time.strftime("%Y-%m-%d-%H-%M-%S-log.txt")
    log_file_path = os.path.join("./LogServer", log_file_name)

    with open(log_file_path, "a") as f:
        f.write(f"Cliente: {addr}, NombreArchivo: {file_name}, TamanioArchivo: {file_size}, "
                f"Tiempo: {tiempo}\n")

    print(f"[SERVER] Cliente {addr} desconectado")

# Iniciar el servidor y aceptar conexiones
def start():
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind(ADDR)
    print(f"[SERVER] Servidor iniciado en {IP}:{PORT}")

    print("Archivos disponibles:")
    for key in FILES:
        print(f"{key} - {FILES[key]}")

    file_key = input("Seleccione el archivo a enviar: ")
    while file_key not in FILES:
        print("Archivo no válido")
        file_key = input("Seleccione el archivo a enviar: ")
    file_name = FILES[file_key]    

    # Manejar múltiples conexiones utilizando hilos
    while True:
        data, addr = server.recvfrom(SIZE)
        client_thread = threading.Thread(target=handle_client, args=(server, addr, file_name))
        client_thread.start()

if __name__ == "__main__":
    start()
