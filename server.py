#!/usr/bin/python3
import http.server, socketserver, os, random
PORT = 8000

if not os.path.exists("files"):
	os.mkdir("files")

class CustomHandler(http.server.SimpleHTTPRequestHandler):
	def do_POST(self):
		content_length = int(self.headers['Content-Length'])
		post_data = self.rfile.read(content_length)

		gfn = str(random.randint(0,pow(2,31)))
		with open("files/" + gfn, 'w') as f:
			f.write(post_data.decode('utf-8'))
		self.send_response(200)
		self.send_header('Content-type', 'text/html')
		self.end_headers()

		self.wfile.write(gfn.encode('utf-8'))

with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
	print(f"Serving file hosting at port {PORT}.")
	print("Send post request to upload a file.")
	print("Ex.: curl -X POST -d 'Content u want to send' 127.0.0.1:8000")
	httpd.serve_forever()
