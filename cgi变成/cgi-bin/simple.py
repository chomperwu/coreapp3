#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cgi
form = cgi.FieldStorage()
text = form.getvalue('text',open('simple.dat').read())
f = open('simple.dat','w')
f.write(text)
f.close()

print '''Content-Type: text/html


<html>
    <head>
        A Simple Editor
    </head>
    <body>
        <form action='simple.py'>
        <textarea rows='10' cols='20' name='text'>%s</textarea><br />
        <input type='submit'>
        </form>
    </body>
</html>
''' % text











