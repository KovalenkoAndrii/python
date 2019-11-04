import os, sys
from http.server import HTTPServer, CGIHTTPRequestHandler

web_directory = '.'
port = 8080

os.chdir('.')
print(os.path.dirname(os.path.realpath(__file__)))
server_address = ("", port)
server_object = HTTPServer(server_address, CGIHTTPRequestHandler)
server_object.serve_forever()
