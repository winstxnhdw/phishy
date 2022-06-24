from sys import argv
from http.server import SimpleHTTPRequestHandler, HTTPServer
from logging import info as loginfo
from logging import basicConfig, INFO

class Server(SimpleHTTPRequestHandler):

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        loginfo(f"POST Request:\nPath: {self.path}\nHeaders:\n{self.headers}\n\nBody:\n{post_data}")
        self.send_response(200)
        self.wfile.write(f"POST request for {self.path.encode('utf-8')}")

def init_server():

    basicConfig(level=INFO, format='%(message)s')
    port = parse_args()
    host = 'localhost'
    httpd = HTTPServer((host, port), Server)

    try:
        loginfo(f"Serving HTTP on {host} port {port} (http://{host}:{port}/) ...")
        httpd.serve_forever()

    except KeyboardInterrupt:
        pass

    finally:
        loginfo("Server closing..")
        httpd.server_close()

def parse_args():

    try:
        return 5000 if len(argv) < 2 else int(argv[1])

    except ValueError:
        loginfo("\nPort must be an integer.\ne.g. python server.py 5000\n")
        raise

if __name__ == '__main__':
    init_server()
