import socket
import threading

HEADER = 64
PORT = 5050
'''I was running the server over wifi and so have used the IPv4 address
    corresponding to wifi. if i run socket.gethostbyname(socket.gethostname())
    on mac it only gives the loopback address 127.0.0.1. It may work on your
    on your system if you're using windows.'''
SERVER = '192.168.29.175'
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

clients = []

def broadcast(msg, sender):
    for client in clients:
        if client != sender:
            client.send(msg)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                print(f"[DISCONNECT] {addr} disconnected.")
                broadcast(f"[DISCONNECT] {addr} disconnected.".encode(FORMAT), conn)
                connected = False
                #break
            else:
                print(f"[{addr}] {msg}")
                broadcast(f"[{addr}] {msg}".encode(FORMAT), conn)

    clients.remove(conn)
    conn.close()




def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        clients.append(conn)
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {len(clients)}")

print("[STARTING] Server is starting...")
start()
