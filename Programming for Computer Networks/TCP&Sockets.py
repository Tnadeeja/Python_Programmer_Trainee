"""
===============================
TCP & SOCKETS – FULL ONE-SHEET
===============================

1. WHAT IS A SOCKET?
-------------------
A socket is one endpoint of a two-way communication link between two programs
running on a network.

• Socket = IP Address + Port Number
• Used for network communication
• Implemented using the socket module in Python

Example:
IP Address : 127.0.0.1 (localhost)
Port       : 1234


2. WHAT IS TCP?
--------------
TCP (Transmission Control Protocol) is a connection-oriented protocol.

Key features:
• Reliable (no data loss)
• Ordered (data arrives in correct order)
• Error-checked
• Uses connection establishment (3-way handshake)

TCP is used when accuracy is more important than speed.
Examples: Web (HTTP), Email, File Transfer


3. TCP CLIENT–SERVER MODEL
--------------------------
• Server waits (listens) for clients
• Client connects to the server
• Data is sent using send()
• Data is received using recv()

One server can handle multiple clients.


4. BASIC TCP COMMUNICATION FLOW
-------------------------------
Server:
1. Create socket
2. Bind IP & port
3. Listen
4. Accept client
5. Send / Receive data
6. Close connection

Client:
1. Create socket
2. Connect to server
3. Send / Receive data
4. Close connection


5. TCP COMMUNICATION DIAGRAM
----------------------------

Client                         Server
------                         ------
socket()  ------------------>  socket()
connect() ------------------>  bind()
                               listen()
                               accept()
send()     ------------------> recv()
recv()     <------------------ send()
close()    ------------------> close()


6. SERVER-SIDE CODE (server.py)
-------------------------------
"""

import socket

# Define server address and port
HOST = '127.0.0.1'   # localhost
PORT = 1234
BUF_SIZE = 1024

# Create TCP socket (AF_INET = IPv4, SOCK_STREAM = TCP)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind socket to IP address and port
server_socket.bind((HOST, PORT))

# Put the server into listening mode
server_socket.listen(1)
print("Server is listening...")

# Accept client connection
client_socket, client_address = server_socket.accept()
print("Connected to client:", client_address)

# Send data to client
message = "Hello Client! This message is from the TCP Server."
client_socket.send(message.encode("utf-8"))

# Close connections
client_socket.close()
server_socket.close()


"""
7. CLIENT-SIDE CODE (client.py)
-------------------------------
"""

import socket

# Define server address and port
HOST = '127.0.0.1'
PORT = 1234
BUF_SIZE = 1024

# Create TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server
client_socket.connect((HOST, PORT))

# Receive data from server
data = client_socket.recv(BUF_SIZE)

# Close connection
client_socket.close()

# Decode and print received message
print(data.decode("utf-8"))


"""
8. IMPORTANT SOCKET FUNCTIONS
-----------------------------
socket()     -> Create a socket
bind()       -> Bind socket to IP and port
listen()     -> Wait for client connections
accept()     -> Accept a client connection
connect()    -> Connect client to server
send()       -> Send data
recv()       -> Receive data
close()      -> Close socket


9. TCP vs UDP (EXAM COMPARISON)
-------------------------------

TCP:
• Connection-oriented
• Reliable
• Ordered data
• Slower
• Uses send() / recv()
• Examples: HTTP, FTP, Email

UDP:
• Connectionless
• Unreliable
• No order guarantee
• Faster
• Uses sendto() / recvfrom()
• Examples: Video streaming, Online games


10. WHY USE TCP SOCKETS?
-----------------------
• Guaranteed data delivery
• Data arrives in correct order
• Error handling
• Suitable for client–server applications

===============================
END OF TCP & SOCKETS ONE-SHEET
===============================
"""