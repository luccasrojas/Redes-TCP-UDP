from socket import *

UDP_IP = "127.0.0.1" # localhost
PORT = 5000
SIZE = 4096
FORMAT = "utf-8"
ADDR = (UDP_IP, PORT)

sock = socket(AF_INET, SOCK_DGRAM)
msg = "Hello, World!"
print(f"[CLIENT] Enviando {msg} a {ADDR}")
sock.sendto(msg.encode(FORMAT), ADDR)

data, addr = sock.recvfrom(SIZE)
print(f"[CLIENT] Recibido {data} de {addr}")
sock.sendto("ACK".encode(FORMAT), addr)

sock.close()
