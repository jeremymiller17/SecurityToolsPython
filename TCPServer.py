# Program creates a TCP server that can support multiple clients.

import socket
import threading

# Server will listen on port '5367' which can be set to any port. And will be open to any IP address
IP = '0.0.0.0'
PORT = 5367


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP, PORT))
    server.listen(10)  # Listens for up to 10 connections.
    print(f'[*] Listening on {IP}:{PORT}')

    while True:
        client, address = server.accept()
        print(f'[*] Accepted connection from {address[0]}:{address[1]}')
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()


def handle_client(client_socket):
    with client_socket as sock:
        request = sock.recv(1024)
        # Prints decoded request from the connected client.
        print(f'[*] Received: {request.decode("utf-8")}')
        # Returns message to connected client
        sock.send(b'Hello Client!')


if __name__ == '__main__':
    main()
