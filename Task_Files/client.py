import socket
import threading

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = '192.168.29.175'
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

connected = True

def receive():
    global connected
    while connected:
        try:
            msg = client.recv(HEADER).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                print("Disconnected from the server.")
                connected = False
                break
            print(msg)
        except:
            pass  # Ignore errors when receiving messages

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)

def start():
    global connected
    thread = threading.Thread(target=receive)
    thread.start()
    while connected:  # Continuously run the loop while the client is connected
        msg = input()
        if connected:  # Only send messages if the client is still connected
            send(msg)
            if msg == DISCONNECT_MESSAGE:
                connected = False  # Update connected flag to indicate disconnection
                break  # Exit the loop if the disconnect message is sent


print("Enter your name:")
name = input()
send(name)

start()

client.close()
