from http.server import HTTPServer
from http.server import BaseHTTPRequestHandler


class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        self.send_response(200)
        self.send_header("User-Agent", "test1")
        self.end_headers()
        bodyLen=int(self.headers.get("content-length"))
        reqBody=str(self.rfile.read(bodyLen).decode("utf-8"))
        print('reqBody:'+reqBody)
        res="<p>Test response<br>Recieved data:<br>"+reqBody
        self.wfile.write(res.encode())

IP="localhost"
PORT=8000
server = HTTPServer((IP, PORT), handler)
server.serve_forever()
