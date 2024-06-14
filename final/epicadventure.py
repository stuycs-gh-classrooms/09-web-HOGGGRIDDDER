#!/usr/bin/python
print('Content-type: text/html\n')

import cgitb #
cgitb.enable() #These 2 lines will allow error messages to appear on a web page in the browser

import cgi

def make_html(title, body):
    html = """
    <!DOCTYPE html>
    <html lang="en">

    <head>
    <meta charset="utf-8">
    """
    html+= '<title>' + title + '</title></head>'
    html+= '<body>' + body + '</body>'
    html+= '</body></html>'
    return html

data = cgi.FieldStorage()

ready = 'Ready'
if ("Ready" in data):
    body += <link href="startepicadventure.css" rel="stylesheet">
    body += '<br><a href="epicadventure.html">Try Again</a>'
    html = make_html("Oasis No. 1", body)

print(html)
