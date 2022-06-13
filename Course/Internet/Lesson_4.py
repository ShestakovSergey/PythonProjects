import http.server

http = http.server.HTTPServer(('', 7999), http.server.CGIHTTPRequestHandler)
http.serve_forever()
