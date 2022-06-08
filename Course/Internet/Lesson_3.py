import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
str = input('Enter string: ')
txt = str.encode('utf-8')
sock.sendto(txt, ('127.0.0.1', 4999))