import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
my_str = input('Enter string: ')
txt = my_str.encode('utf-8')
sock.sendto(txt, ('127.0.0.1', 4999))
