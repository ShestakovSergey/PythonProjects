import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('10.0.1.45', 8888))
sock.listen(5)
print('Waiting connect...')

while True:
    try:
        client, addr = sock.accept()
    except KeyboardInterrupt:
        sock.close()
        break
    else:
        result = client.recv(4096)
        client.close()
        print('Print message:', result.decode('utf-8'))
