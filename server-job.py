from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from SocketServer import ThreadingMixIn
import os

list_client_responses = []

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    pass

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        global running
        if self.path == '/':
            self.send_file()
        elif self.path.startswith('/calculation'):
            self.send_calculation()
        elif self.path.startswith('/quit'):
            self.send_response(200)
            print sum(list_client_responses)

    def send_file(self):
        # Check to see if file exists and is a file, not directory
        filename = 'text.txt'
        if os.path.isfile(filename):
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()

            # Read and send the contents of the file
            with open(filename) as f:
                contents = f.read()
            self.wfile.write(contents)
        else:
            self.send_response(404)
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()
            self.wfile.write('Dude! File not found')

    def send_calculation(self):
        empty, operation, number = self.path.split('/')
        result = int(number)
        list_client_responses.append(result)
        self.send_response(200)
        self.send_header('Content-Type', 'text/plain')
        self.end_headers()
        self.wfile.write(result)

running = True
server = ThreadedHTTPServer(('', 9000), MyHandler)
print 'Server started on host:{0}, port:{1}'.format(*server.server_address)
while running:
    server.handle_request()