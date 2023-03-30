from socket import *

PORT = 5000
SIZE = 4096
FORMAT = "utf-8"
IP = gethostbyname(gethostname())
ADDR = (IP, PORT)

socket = socket(AF_INET, SOCK_DGRAM)
socket.bind(ADDR)

print(f"[SERVER] Servidor iniciado en {ADDR}")

while True:
    data, addr = socket.recvfrom(SIZE)
    print(f"[SERVER] Recibido {data} de {addr}")
    socket.sendto("ACK".encode(FORMAT), addr)
