import socket

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    print('4999 is bind')
    sock.bind(('127.0.0.1', 4999))
    while True:
        print('Waiting connect...')
        result = sock.recv(4096)
        print('Message', result.decode('utf-8'))
