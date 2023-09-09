import http.server
import socketserver

class MyHandler(http.server.SimpleHTTPRequestHandler):
    # Define a dictionary to map routes to functions
    routes = {
        '/login': handle_login,
        '/dashboard': handle_dashboard,
        '/redirect': handle_redirect,
        
    }

    def do_GET(self):
        # Get the requested path
        path = self.path

        # Check if the path is in the routes dictionary
        if path in self.routes:
            # Call the corresponding function or handler
            self.routes[path](self)
        else:
            # Handle other routes here
            super().do_GET()

    # Define handlers for specific routes
    def handle_login(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'Login Page')

    def handle_dashboard(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'Dashboard Page')
    
    def handle_redirect(self):
        # Perform the redirection
        self.send_response(302)  # 302 Found
        self.send_header('Location', '/dashboard')  # Redirect to /dashboard
        self.end_headers()
        
def main():
    PORT = 8000
    with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
        print(f"Serving at http://localhost:{PORT}")
        httpd.serve_forever()

if __name__ == "__main__":
    main()
