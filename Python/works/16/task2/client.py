import socket

HOST = 'localhost'
PORT = 50007

print("client")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while True:
    msg = input()
    s.sendall(msg.encode())

    if msg == 'end':
        break

s.close()