import http.server
import socketserver

# Define the request handler class
class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Respond with "Hello, World!"
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"Hello, World!")

# Define the server address and port
PORT = 8000

# Create the HTTP server
with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print(f"Serving on port {PORT}")
    httpd.serve_forever()
