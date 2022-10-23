# Program to make TCP requests

import socket

# Destination variables(Configured to connect to TCPServer.py)
target_host = "127.0.0.1"
target_port = 5367

# Create a socket object. A socket is an ip address coupled with a port number.
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect client to target.
client.connect((target_host, target_port))

# Use connection to send HTTP request to target. Example:
# client.send(b"GET / HTTP/1.1\r\nHost: github.com\r\n\r\n")

# Uses connection to send message to TCPServer.py
client.send(b"Hello server from TCPClient.py")

# Receive http response.
res = client.recv(4096)

# Prints response. Notice if '301' is returned. This is a redirect to the 'https' version,
print(res.decode())
client.close()
