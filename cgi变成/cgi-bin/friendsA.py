#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cgi

reshtml = '''Content-Type: text/html


<html><head><title>
Friends CGI Demo(dynamic)
</title></head>
<body><H3>Friends list for: <I>%s<I></H3>
Your name is: <B>%s</B>
You have <B>%s</B> friends.
</body></html>
'''

form = cgi.FieldStorage()
who = form['person'].value
#who = form.getvalue('person')
howmany = form.getvalue('howmany')
print reshtml % (who,who,howmany)










