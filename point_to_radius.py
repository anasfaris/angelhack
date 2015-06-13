# function has 2 args: point, radius
# returns list of poi's within the radius
import foursquare
from shapely.geometry import *

def point_to_radius(point, radius):
	print ("in point_to_radius function")
	point = Point(0.0,0.0)
	print (point.length)
	client = foursquare.Foursquare(client_id='CHZK02QJLL25G1E2JO30AKSQPEMOSRS1UJ1S10TLTMXQJNBH', client_secret='GBIBO01JLAMT4LBVHMD5VUHMPCFTAXHEKBEUZHMG4Y5TYARJ')
	myVenues = client.venues.search(params={'query': 'coffee', 'll': '40.7,-73.9'})
	print(type(myVenues['venues']))
	#print(myVenues[0])
	#for index in myVenues:
		#print(index.keys())
	






	return "list of poi's from point %s within radius " %point