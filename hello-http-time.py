#!/usr/bin/env python3

import time
import fileinput

import SimpleHTTPServer
import SocketServer

message = "Starting HTTP Server ... "
PORT=8081

stext = "<TIME>"
rtext = "Hello, HTTP Server at: {}, Time is: {} ".format(PORT, time.strftime("%c"))

for line in fileinput.input("index.html", inplace=True):
    print(line.replace(stext, rtext).rstrip('\r\n'))

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

print message, PORT
httpd.serve_forever()

