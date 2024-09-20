from socket import socket, SOCK_STREAM, AF_INET


def main():
    server_sock = socket(AF_INET, SOCK_STREAM)
    server_addr = ('192.168.1.23', 55_000)
    print(f'trying to connect to the server at address {server_addr}')
    server_sock.connect(server_addr)

    # we can send/recv bytes to/from the server (in tandem)
    msg = server_sock.recv(1024).decode()
    print(f'Server says: {msg}')

    filename = input('Enter the file you want from the server: ')
    server_sock.send(filename.encode())
    content = server_sock.recv(3000).decode()
    print(content)


if __name__ == '__main__':
    main()
    
