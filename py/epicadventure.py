#!/usr/bin/python
print('Content-type: text/html\n')

import cgitb #
cgitb.enable() #These 2 lines will allow error messages to appear on a web page in the browser

import cgi


HTML_HEADER = """
<!DOCTYPE html>
<html lang="en">

<head>
<meta charset="utf-8">
<title>The Beginning...</title>
</head>
"""

HTML_FOOTER = """
</body>
</html>
"""


from random import random

print ("your lucky number is:" + str(random()))