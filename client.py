import socket

HOST = "" # localhost(127.0.0.1) by default
PORT = 46572

TIMEOUT = 10

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    client_socket.settimeout(TIMEOUT)
    client_socket.sendto(b'1', (HOST, PORT))
    date, address = client_socket.recvfrom(1024)
    print(f"Server time: {date.decode()}")

except socket.timeout:
    print("[-] Timeout error\nPossible reasons:\n\
    - Server doesn't response\n\
    - Bad network connection")
except socket.error as e:
    print(f"[-] {e}")
finally:
    client_socket.close()