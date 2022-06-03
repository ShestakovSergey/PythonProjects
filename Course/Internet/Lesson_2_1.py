import os
import socket

unix_sock_name = 'unix.sock'
sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)

if os.path.exists(unix_sock_name):
    os.remove(unix_sock_name)

sock.bind(unix_sock_name)
print('Waiting connect....')

while True:
    try:
        result = sock.recv(4096)
    except KeyboardInterrupt:
        sock.close()
        break
    else:
        print('Message:', result.decode('utf-8'))
