import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
str = input('Enter string: ')
txt = str.encode('utf-8')
sock.sendto(txt, ('10.0.1.48', 4999))