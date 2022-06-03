import socket

sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
my_str = input('Enter string: ')
txt = my_str.encode('utf-8')
sock.sendto(txt, 'unix.sock')
