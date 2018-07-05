#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

m = re.match("b","bcdef")
print m.group()

n = re.search('\w+.google(?=.com)','www.google.com')
print n.group()

print re.search('\w+.google(?=.cn)','www.google.com')
#\w+.google后面要跟.cn才匹配\w+.google。所以这个是None

z = re.search('(?!.cn)cn','www.google.cn')
print z.group()

print re.findall('th\w+','the one is this!')

me = re.compile('''(?x)
    \((\d{3})\)  #3个数字
    [ ]           #空白字符
    (\d{3})
    -
''')
print me.search('(800) 555-1212').group()






