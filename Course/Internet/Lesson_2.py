import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('0.0.0.0', 8888))
print('Waiting connect....')

while True:
    try:
        result = sock.recv(4096)
    except KeyboardInterrupt:
        sock.close()
        break
    else:
        print('Message:', result.decode('utf-8'))
