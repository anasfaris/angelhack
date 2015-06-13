#find middle location between the two people
#assuming we already have the latitude & longitude of both two people

#example location person 1
latitude1 = 3.1385059    
longitude1 = 101.6869895
location1 = [str(latitude1) , str(longitude1)]

#example location person 2
latitude2 = 3.0863121   
longitude2 = 101.5765254
location2 = [str(latitude2), str(longitude2)]


from geopy.geocoders import Nominatim
from geopy.distance import vincenty


def fetch_address1():
	global location_1
	geolocator = Nominatim()
	location_1 = geolocator.reverse(location1)
	print ("Your location:")
	print(location_1.address)
	print (" ")

def fetch_address2():
	global location_2
	geolocator = Nominatim()
	location_2 = geolocator.reverse(location2)
	print ("Your friend's location:")
	print(location_2.address)
	print (" ")

def where_is_the_middle():
	latitude_middle = (latitude1 + latitude2)/2
	longitude_middle = (longitude1 + longitude2)/2
	location_middle = [latitude_middle, longitude_middle]
	geolocator = Nominatim()
	locationmiddle = geolocator.reverse(location_middle)
	print ("Where should you two meet?")
	print(locationmiddle)
	print (" ")

fetch_address1()
fetch_address2()
where_is_the_middle()