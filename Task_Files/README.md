# 🖧 Server-Client Chatroom System

A lightweight, real-time chatroom system built in Python using socket programming and multi-threading. This project enables multiple users on the same local network to exchange text messages via a central server.

---

## 🚀 Features

- Multi-client support using Python threading
- Real-time message broadcasting to all connected users
- Graceful handling of client disconnections
- Lightweight and dependency-free (uses Python standard libraries)

---

## 🛠️ Technologies Used

- Python 3
- `socket` – for TCP/IP network communication
- `threading` – for concurrent client handling

---

## 📁 Project Structure
Server-Client-System/
├── server.py # Main server that accepts and manages clients
├── client.py # Client script to connect and chat with server


---

## 🧪 How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/AdityaGoel0330/Server-Client-System.git
cd Server-Client-System
```
### 2. Run the Server
Start the server on the host machine:
```bash
python server.py
```

### 3. Run the Client(s)
On the same or another machine on the same network, run:
```bash
python client.py
```
🔁 Repeat this step for each user who wants to join the chatroom.

---

## 🧠 How It Works
The server listens for incoming TCP connections on a specified port.
Each client connection is handled on a separate thread.
Messages received from one client are broadcast to all other connected clients.
The client maintains a loop for sending and receiving messages.

---

## ✅ Example Output
```
[You] Hello everyone!
[Alice] Hi! Glad to be here.
[Bob] Hey folks!
```

---

## 📌 Notes
Ensure all machines are on the same local network (LAN/Wi-Fi).
Your firewall or antivirus may block local ports — allow access if prompted.
This is a basic prototype. For production use, consider:
Encrypted communication (e.g., TLS/SSL)
Robust message delivery protocols
WebSocket or async I/O support for scaling

---
