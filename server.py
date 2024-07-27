import socket
from datetime import datetime

HOST = "0.0.0.0"
PORT = 46572

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))

try:
    while True:
        data, address = server_socket.recvfrom(1) # Some byte data
        server_socket.sendto(f"{datetime.now().strftime("%Y-%m-%d %H:%M:%S:%f")}".encode(), address)
except KeyboardInterrupt:
    print("Server shutdown...")
except Exception as e:
    print(e)
finally:
    server_socket.close()
