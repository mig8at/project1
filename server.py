from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Hola, este es un servidor basico en Python!')
        
httpd = HTTPServer(('0.0.0.0', int(os.environ.get('PORT', 8080))), SimpleHTTPRequestHandler)
httpd.serve_forever()