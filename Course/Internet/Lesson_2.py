import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('10.0.1.48', 4999))
print('Waiting connect....')

while True:
    try:
        result = sock.recv(4096)
    except KeyboardInterrupt:
        sock.close()
        break
    else:
        print('Message:', result.decode('utf-8'))
