"""
HTTP Web Service for Prime Number Application
Deployable on Kubernetes with health checks and JSON endpoints.
Uses Python standard library (no pip dependencies required).
"""

import sys
import os
from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import urllib.parse

# Ensure local folder is in Python search path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from prime import get_prime_details, is_prime

PORT = 8000

class PrimeRequestHandler(BaseHTTPRequestHandler):
    def _send_json_response(self, status_code: int, data: dict):
        self.send_response(status_code)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(json.dumps(data, indent=2).encode('utf-8'))

    def do_GET(self):
        parsed_url = urllib.parse.urlparse(self.path)
        path = parsed_url.path
        query_params = urllib.parse.parse_qs(parsed_url.query)

        # Health endpoint for Kubernetes liveness & readiness probes
        if path in ('/healthz', '/health'):
            self._send_json_response(200, {"status": "UP", "service": "prime-service"})
            return

        # Prime check endpoint: /check?num=17 or /prime?n=17
        if path in ('/check', '/prime'):
            num_param = query_params.get('num') or query_params.get('n')
            if not num_param:
                self._send_json_response(400, {
                    "error": "Missing parameter 'num'. Example: /check?num=23"
                })
                return

            try:
                num = int(num_param[0])
                details = get_prime_details(num)
                self._send_json_response(200, details)
            except ValueError:
                self._send_json_response(400, {
                    "error": f"Invalid integer '{num_param[0]}'"
                })
            return

        # Default info endpoint
        self._send_json_response(200, {
            "message": "Welcome to Prime Number Kubernetes Microservice",
            "usage": "/check?num=<integer>",
            "health_check": "/healthz",
            "example": "/check?num=29"
        })

    def log_message(self, format, *args):
        print(f"[HTTP Server] {self.address_string()} - {format % args}")

def run():
    server_address = ('', PORT)
    httpd = HTTPServer(server_address, PrimeRequestHandler)
    print(f"Prime Number HTTP service running on port {PORT}...")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server...")
        httpd.server_close()

if __name__ == '__main__':
    run()
