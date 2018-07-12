#!/usr/bin/env python
# -*- coding: utf-8 -*-


import socket

tcpclisock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
tcpclisock.connect(('127.0.0.1',8000))

while True:
    data = raw_input('> ')
    if not data:
        break
    tcpclisock.send(data)
    data = tcpclisock.recv(1024)
    if not data:
        break
    print data
tcpclisock.close()
