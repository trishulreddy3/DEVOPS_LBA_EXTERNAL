"""
Arithmetic Microservice for Kubernetes Deployment
Provides health checks and arithmetic calculation REST endpoints.
Uses Python standard library (no external pip dependencies).
"""

import sys
import os
from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import urllib.parse

# Ensure local folder is in Python search path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from arithmetic import compute

PORT = 8080

class ArithmeticHandler(BaseHTTPRequestHandler):
    def _send_json_response(self, status_code: int, data: dict):
        self.send_response(status_code)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(json.dumps(data, indent=2).encode('utf-8'))

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path
        params = urllib.parse.parse_qs(parsed.query)

        # Health endpoint
        if path in ('/healthz', '/health'):
            self._send_json_response(200, {"status": "UP", "service": "arithmetic-service"})
            return

        # Calculation endpoint: /calc?op=add&a=10&b=20
        if path == '/calc':
            op = params.get('op', [None])[0]
            a_val = params.get('a', [None])[0]
            b_val = params.get('b', [None])[0]

            if not op or a_val is None or b_val is None:
                self._send_json_response(400, {
                    "error": "Missing parameters. Required: op, a, b",
                    "example": "/calc?op=add&a=15&b=25"
                })
                return

            try:
                a = float(a_val)
                b = float(b_val)
                result = compute(op, a, b)
                if result.is_integer():
                    result = int(result)
                self._send_json_response(200, {
                    "operation": op,
                    "a": a,
                    "b": b,
                    "result": result
                })
            except ValueError as e:
                self._send_json_response(400, {"error": str(e)})
            except ZeroDivisionError as e:
                self._send_json_response(400, {"math_error": str(e)})
            return

        # Default info endpoint
        self._send_json_response(200, {
            "message": "DevOps Lab - Arithmetic Operations API",
            "health_check": "/healthz",
            "endpoints": {
                "calculate": "/calc?op=<add|sub|mul|div>&a=<num>&b=<num>"
            },
            "examples": [
                "/calc?op=add&a=10&b=25",
                "/calc?op=mul&a=7&b=8",
                "/calc?op=div&a=100&b=4"
            ]
        })

def run():
    server = HTTPServer(('', PORT), ArithmeticHandler)
    print(f"Arithmetic HTTP Service listening on port {PORT}...")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server...")
        server.server_close()

if __name__ == '__main__':
    run()
