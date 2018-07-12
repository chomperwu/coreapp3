#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

while True:
    tcpclisock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcpclisock.connect(('127.0.0.1', 8000))
    data = raw_input('> ')
    if not data:
        break
    tcpclisock.send('%s\r\n' % data)
    data = tcpclisock.recv(1024)
    if not data:
        break
    print data
    tcpclisock.close()





