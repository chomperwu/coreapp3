#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading
from time import ctime

class MyThread(threading.Thread):
    def __init__(self,func,args,name=''):    #这个类实例化至少需要2个参数func,args
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args

    def getResult(self):
        return self.res

    def run(self):
        print 'Starting',self.name,'at:',ctime()
        self.res = self.func(*self.args)   #*self.args是一个元组
        print self.name,'finished at:',ctime()

