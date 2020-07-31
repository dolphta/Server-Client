import socket

host = "127.0.0.1"
port = 2121

with socket.socket() as s:
    s.bind((host, port))
    s.listen()
    conn, addr = s.accept()

    with conn:
        print("Communication succesful:", addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)