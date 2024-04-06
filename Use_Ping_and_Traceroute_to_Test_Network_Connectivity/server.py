import socket

HEADER = 64
FORMAT = "utf-8"
SERVER = socket.gethostbyname(socket.gethostname())
PORT = 5050
DISCONNECT_MSG = "End"
ADDR = (SERVER, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

print("server is starting...")

server.listen()
print("server is listening on ", SERVER)

while True:
    conn, addr = server.accept()
    print("connected to ", addr)
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MSG:
                connected = False
                conn.send(f"Terminating connection with {addr}".encode(FORMAT))
            else:
                print(msg)
                conn.send("Message received".encode(FORMAT))
    conn.close()


