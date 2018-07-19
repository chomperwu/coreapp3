#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading
from time import sleep,ctime

loops = [4,2]

def loop(nloop,nsec):
    print 'start loop',nloop,'at:',ctime()
    sleep(nsec)
    print 'loop',nloop,'done at:',ctime()

def main():
    print 'starting at:',ctime()
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        t = threading.Thread(target=loop,args=(i,loops[i]))  #生成线程
        threads.append(t)   #把线程保存到列表中

    for i in nloops:
        threads[i].start()    #开启线程

    for i in nloops:
        threads[i].join()   #主线程在这里要等待所有线程执行完毕才能继续执行

    print 'all DONE at:',ctime()   #这是主线程

if __name__ == '__main__':
    main()