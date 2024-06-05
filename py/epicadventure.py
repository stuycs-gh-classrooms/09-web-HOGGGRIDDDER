#!/usr/bin/python
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
<link href="startepicadventure.css" rel="stylesheet">
<title>Hello</title>
</head>
"""

HTML_FOOTER = """
</body>
</html>
"""


data = cgi.FieldStorage()

html= HTML_HEADER
html+= '<br><a href="hello.html">Try Again</a>'
html+= HTML_FOOTER
print(html)
