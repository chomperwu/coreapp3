#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
from time import ctime

tcpsocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#socket.AF_INET指网络套接字。socket.AF_UNIX指unix套接字
#socket.SOCK_STREAM指tcp。SOCK_DGRAM指udp

tcpsocket.bind(('127.0.0.1',8000))
tcpsocket.listen(5)

while True:
    print 'waiting for connection...'
    tcpclisock,addr = tcpsocket.accept()
    print 'connected from:',addr

    while True:
        data = tcpclisock.recv(1024)
        if not data:
            break
        tcpclisock.send('%s %s' % (ctime(),data))
    tcpclisock.close()
tcpsocket.close()


