#!/usr/bin/env python
# -*- coding: utf-8 -*-

from twisted.internet import protocol,reactor
from time import ctime

class TSServProtocol(protocol.Protocol):
    def connectionMade(self):
        clnt = self.clnt = self.transport.getPeer().host
        print 'connected from:',clnt
    def dataReceived(self, data):
        print 'sending %s' % data
        self.transport.write('%s %s' % (ctime(),data))

factory = protocol.Factory()
factory.protocol = TSServProtocol
print 'waiting for connection..'
reactor.listenTCP(8000,factory)
reactor.run()



