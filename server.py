import socket

SERVER_IP = '103.94.69.52'
SERVER_PORT = 888
ADDR = (SERVER_IP,SERVER_PORT)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(ADDR)
