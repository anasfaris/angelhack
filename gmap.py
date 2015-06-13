# from googlemaps import *

# gmaps = googlemaps.Client(key='AIzaSyDNY9na8tviZNcpXbgBr9L-V39BtomIMy4')

# # Geocoding and address
# geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

# # Look up an address with reverse geocoding
# reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

# # Request directions via public transit
# now = datetime.now()
# directions_result = gmaps.directions("Sydney Town Hall",
#                                      "Parramatta, NSW",
#                                      mode="transit",
#                                      departure_time=now)

# def get_direction():

# 	print "geocode_result:"
# 	print geocode_result

# 	print "reverse_geocode_result:"
# 	print reverse_geocode_result

# 	print "directions_result"
# 	print directions_result

# 	return directions_result

from googlemaps import GoogleMaps

mapService = GoogleMaps()

directions = mapService.directions('texarkana', 'atlanta')

print directions