import http.server
import socketserver

PORT = 8000

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/login':
            # Perform authentication checks here
            authenticated = True  # Example: Set this to True if authentication succeeds

            if authenticated:
                # Redirect to the dashboard upon successful login
                self.send_response(302)
                self.send_header('Location', '/dashboard')
                self.end_headers()
            else:
                # Redirect to the login page with an error message
                self.send_response(302)
                self.send_header('Location', '/login_page?error=True')
                self.end_headers()
        else:
            # Handle other routes here
            super().do_GET()

def main():
    with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
        print(f"Serving at http://localhost:{PORT}")
        httpd.serve_forever()

if __name__ == "__main__":
    main()
