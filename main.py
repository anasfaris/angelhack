#Gevent Server
import sys
if 'threading' in sys.modules:
    del sys.modules['threading']
# from gevent import monkey; monkey.patch_all()

# try googlemaps
from gmap import get_direction

get_direction()


#Bottle Framework
from bottle import *
import bottle
import os
from point_to_radius import *

#specifying the path for the files
@route('/static/<filepath:path>')
def server_static(filepath):
	return static_file(filepath, root='.')

@error(404)
def error404(error):
    return 'URL does not exist'

@route("/")
def main():
	return template('index.html')
	
point_to_radius(0, 0)

run(reloader=True, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
