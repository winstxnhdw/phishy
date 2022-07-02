from json import loads, dumps
from sys import argv
from http.server import SimpleHTTPRequestHandler, HTTPServer

class Server(SimpleHTTPRequestHandler):

    def do_POST(self):

        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        formatted_data = '\n'.join(line.strip() for line in dumps(loads(post_data), indent=2).lstrip('{').rstrip('}').split('\n'))
        print(f"\nPOST\n{self.headers}Body:\n{formatted_data}")
        self.send_response(200)

def init_server():

    port = parse_args()
    host = 'localhost'
    httpd = HTTPServer((host, port), Server)

    try:
        httpd.serve_forever()
        print(f"Serving HTTP on {host} port {port} (http://{host}:{port}/)..")

    except KeyboardInterrupt:
        print("Manual exit detected.")

    finally:
        httpd.server_close()
        print("\nServer closing..")

def parse_args():

    try:
        return 5000 if len(argv) < 2 else int(argv[1])

    except ValueError:
        print("\nPort must be an integer.\ne.g. python server.py 5000\n")
        raise

if __name__ == '__main__':
    init_server()
