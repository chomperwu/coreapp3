#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os,re
f = os.popen('tasklist /nh','r')

for eachline in f:
        print re.findall(
            r'([\w.]+(?: [\w.]+)*)\s\s+(\d+) \w+\s\s+\d+\s\s+([\d,]+ K)',eachline.rstrip()
    )
f.close()



