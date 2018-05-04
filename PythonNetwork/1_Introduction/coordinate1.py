from pygeocoder import Geocoder
import requests

if __name__ == '__main__':
	# use package pygeocoder
	address = '207 N. Defiance St, Archbold, OH'
	print(Geocoder.geocode(address)[0].coordinates)


	# use Requests
	base = 'https://maps.googleapis.com/maps/api/geocode/json'
	params = {
		'address': address,
		'sensor': 'false'
	}
	response = requests.get(base, params=params)
	answer = response.json()
	print(answer['results'][0]['geometry']['location'])