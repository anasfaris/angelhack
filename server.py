import os
<<<<<<< HEAD
import http.client
=======
>>>>>>> 326a7363803dd1a2e29d4ca80fb7c09f816b5a7c
try:
  from SimpleHTTPServer import SimpleHTTPRequestHandler as Handler
  from SocketServer import TCPServer as Server
except ImportError:
  from http.server import SimpleHTTPRequestHandler as Handler
  from http.server import HTTPServer as Server

# Read port selected by the cloud for our application
PORT = int(os.getenv('VCAP_APP_PORT', 8000))
# Change current directory to avoid exposure of control files
os.chdir('static')

httpd = Server(("", PORT), Handler)
try:
  print("Start serving at port %i" % PORT)
  httpd.serve_forever()
except KeyboardInterrupt:
  pass
<<<<<<< HEAD

conn = http.client.HTTPConnection("http://ratemyarticle.mybluemix.net/")
=======
>>>>>>> 326a7363803dd1a2e29d4ca80fb7c09f816b5a7c
httpd.server_close()

