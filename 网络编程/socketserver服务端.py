#!/usr/bin/env python
# -*- coding: utf-8 -*-

from SocketServer import TCPServer,StreamRequestHandler
from time import ctime

class MyRequestHandler(StreamRequestHandler):
    def handle(self):
        print 'connected from:',self.client_address
        self.wfile.write('%s %s' % (ctime(),self.rfile.readline()))

tcpServ = TCPServer(('127.0.0.1',8000),MyRequestHandler)
print 'waiting for connection...'
tcpServ.serve_forever()



