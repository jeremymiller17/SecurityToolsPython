# Program to make UDP(User datagram protocol) requests
import socket

# Destination variables
target_host = "127.0.0.1"
target_port = 80

# Create a socket object. A socket is an ip address coupled with a port number.
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Since there is no connection with UDP, just send the data.
client.sendto(b"Testing UDP!", (target_host, target_port))

# Receive a response
data, addr = client.recvfrom(4096)

print(str(data))
