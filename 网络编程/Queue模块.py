#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Queue

q = Queue.Queue(3)

for i in [0,2,3]:
    q.put('inter')
q.put('jojo')
print q
print q.get_nowait()
print q.get_nowait()
print q.get_nowait()
print q.get(1)