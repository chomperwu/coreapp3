#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

m = re.match("b","bcdef")
print m.group()

print re.search('th(\w+)','the one is this!').group()
#返回整个匹配对象 the
print re.search('th(\w+)','the one is this!').group(1)
#返回匹配的子组  e


n = re.search('\w+.google(?=.com)','www.google.com')
print n.group()

print re.search('\w+.google(?=.cn)','www.google.com')
#\w+.google后面要跟.com才匹配www.google.com。所以这个是None

z = re.search('google(?!.cn)','www.google.com')
print z.group()

print re.findall('th\w+','the one is this!')
print re.findall('th(\w+)','the one is this!')
print re.findall('th(\w+) (one)','the one is this one!')


"""
me = re.compile('''(?x)
    \((\d{3})\)  #3个数字
    [ ]           #空白字符
    (\d{3})
    -
''')
print me.search('(800) 555-1212').group()
"""






