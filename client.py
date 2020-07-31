import socket

host = "127.0.0.1"
port = 2121

with socket.socket() as s:
    s.connect((host, port))
    s.sendall(b"Hello world!")
    data = s.recv(1024)

print(data)