import socket
import threading
import hashlib
import os
import time

# Puerto de escucha del servidor
PORT = 12345
HOST = ''

# Directorio donde se encuentran los archivos
FILE_DIR = "./Files"

# Archivos disponibles para envío
FILES = {
    "file1": "file1.txt",
    "file2": "file2.txt"
}

# Función para manejar la conexión con el cliente
def handle_client(conn, addr, file_name):
    print(f"[SERVER] Cliente conectado desde {addr}")

    # Abrir archivo y enviar datos
    file_path = os.path.join(FILE_DIR, file_name)
    file_size = os.path.getsize(file_path)

    with open(file_path, "rb") as f:
        data = f.read()
        conn.sendall(data)

    # Calcular hash del archivo
    hash_value = hashlib.md5(data).hexdigest()
    conn.sendall(hash_value.encode())

    # Recibir confirmación de recepción
    confirmation = conn.recv(1024).decode()

    # Registro de la conexión en el archivo de logs
    log_file_name = time.strftime("%Y-%m-%d-%H-%M-%S-log.txt")
    log_file_path = os.path.join("Logs", log_file_name)

    with open(log_file_path, "a") as f:
        f.write(f"Cliente: {addr}, Archivo: {file_name}, Tamaño: {file_size}, "
                f"Hash: {hash_value}, Confirmación: {confirmation}\n")

    print(f"[SERVER] Cliente {addr} desconectado")

# Función para esperar conexiones entrantes
def wait_for_connections(sock, file_name, num_connections):
    threads = []
    for i in range(num_connections):
        conn, addr = sock.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr, file_name))
        threads.append(thread)
    for thread in threads:
        thread.start()

# Función principal del servidor
def main():
    # Crear socket del servidor
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind(("", PORT))
        sock.listen()

        print(f"[SERVER] Escuchando en el puerto {PORT}")

        # Pedir al usuario que seleccione el archivo a enviar
        print("Archivos disponibles:")
        for key in FILES:
            print(f"{key} - {FILES[key]}")

        file_key = input("Seleccione el archivo a enviar: ")
        while file_key not in FILES:
            print("Archivo no válido")
            file_key = input("Seleccione el archivo a enviar: ")

        file_name = FILES[file_key]

        # Pedir al usuario que seleccione el número de conexiones
        num_connections = int(input("Seleccione el numero de conexiones a aceptar: "))

        # Esperar conexiones entrantes
        wait_for_connections(sock, file_name, num_connections)

if __name__ == "__main__":
    main()