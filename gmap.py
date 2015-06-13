from googlemaps import *

gmaps = googlemaps.Client(key='AIzaSyAkgMRXumOP9CkZD7JIXaCl_W4KPU2Kbqk')

# Geocoding and address
geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

# Look up an address with reverse geocoding
reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

# Request directions via public transit
now = datetime.now()
directions_result = gmaps.directions("Sydney Town Hall",
                                     "Parramatta, NSW",
                                     mode="transit",
                                     departure_time=now)

def get_direction():

	print "geocode_result:"
	print geocode_result

	print "reverse_geocode_result:"
	print reverse_geocode_result

	print "directions_result"
	print directions_result

	return directions_result
