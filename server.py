
import socket
from tqdm import tqdm
import threading
import os
import hashlib
import time
 
IP = socket.gethostbyname(socket.gethostname())
PORT = 4456
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

def handle_client(conn, addr, file_name,barrier):

    #Establecer la conexion con el cliente
    print(f"[SERVER] Cliente conectado desde {addr}")
    #Recibe que esta listo para conectarse
    conn.recv(SIZE)
    #Envia que esta listo para mandar
    conn.send("Data received.".encode(FORMAT))
    """ Receiving the filename and filesize from the client. """

    #Comenzar el envio del archivo
    print("Cliente en espera")
    barrier.wait()
    
    # Abrir archivo y enviar datos
    file_path = os.path.join(FILE_DIR, file_name)
    file_size = os.path.getsize(file_path)

    print("Enviando archivo de tamaño", file_size, "bytes")
    counter = 0
    with open(file_path, "rb") as f:
        t1 = time.time()
        while True:
            data = f.read(SIZE)
            if not data:
                break
            conn.sendall(data)
            conn.recv(SIZE)
            counter += 1
    print(counter)
    conn.sendall(b"FIN")
    conn.recv(SIZE)
        
    print("Archivo enviado")
    
    #ACK llego el archivo
    conn.recv(SIZE)
    print("El archivo fue recibido")
    t2 = time.time()
    tiempo = t2-t1

    # Calcular hash del archivo
    with open(file_path, "rb") as f:
        md5 = hashlib.md5()
        for chunk in iter(lambda: f.read(4096), b""):
            md5.update(chunk)
        hash_value =md5.hexdigest()

    print("Enviando hash")
    conn.sendall(hash_value.encode())

    print("Esperando confirmación")
    # Recibir confirmación de recepción
    confirmation = conn.recv(1024).decode()

    # Registro de la conexión en el archivo de logs
    log_file_name = time.strftime("%Y-%m-%d-%H-%M-%S-log.txt")
    log_file_path = os.path.join("./Logs", log_file_name)

    with open(log_file_path, "a") as f:
        f.write(f"Cliente: {addr}, Archivo: {file_name}, Tamaño: {file_size}, "
                f"Hash: {hash_value}, Confirmación: {confirmation}, Tiempo: {tiempo}\n")
    conn.close()
    print(f"[SERVER] Cliente {addr} desconectado")

    

def manage_connections(sock, num_connections):
    barrier = threading.Barrier(num_connections)
    threads = []
    counter = 0

    print("Archivos disponibles:")
    for key in FILES:
        print(f"{key} - {FILES[key]}")

    file_key = input("Seleccione el archivo a enviar: ")
    while file_key not in FILES:
        print("Archivo no válido")
        file_key = input("Seleccione el archivo a enviar: ")
    file_name = FILES[file_key]

    while counter < num_connections:
        conn, addr = sock.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr, file_name,barrier))
        threads.append(thread)
        """ Accepting the connection from the client. """
        # Pedir al usuario que seleccione el archivo a enviar
        counter+=1

    for thread in threads:
        thread.start()

def main():
    """ Creating a TCP server socket """
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen()
    num_conexiones = int(input("Ingrese el numero de conexiones: "))
    
    print("[+] Listening...")
    manage_connections(server, num_conexiones)
    server.close()
 
if __name__ == "__main__":
    main()