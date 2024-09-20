from os import listdir
from socket import socket, SOCK_STREAM, AF_INET
import threading

files = listdir('.')
files = [file for file in files if file.endswith('.py')]
files = ', '.join(files)

def handle_client(client_sock, client_addr):
    global files
    print(f'got a connection from a client at address {client_addr}')
    msg = f'You can ask for these files: {files}'
    client_sock.send(msg.encode())
    filename = client_sock.recv(1024)
    with open(filename) as file:
        content = file.read()
        client_sock.send(content.encode())

    client_sock.close()


def main():
    server_sock = socket(AF_INET, SOCK_STREAM)
    server_addr = ('192.168.1.23', 55_000)
    server_sock.bind(server_addr)

    server_sock.listen()
    print(f'server listening at address {server_addr}')

    while True:
        print('waiting for client connection...')
        client_sock, client_addr = server_sock.accept()
        # handle_client(client_sock, client_addr)
        threading.Thread(target=handle_client, args=(client_sock, client_addr)).start()


if __name__ == '__main__':
    main()
    
