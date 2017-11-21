#!/usr/bin/env python

import socket

TCP_IP = '10.0.0.201'
TCP_PORT = 5005
BUFFER_SIZE = 1024
MESSAGE = b'Hello, world!'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(MESSAGE)
data = s.recv(BUFFER_SIZE)
s.close()

print("received_data:", data)
