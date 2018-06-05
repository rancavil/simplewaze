import sys

if sys.version_info > (3,):
	import urllib.request as urllib
else:
	import urllib

import json
import config

def getRouteTimes(debug = False):
	try:
		f = urllib.urlopen(config.urlwaze)
		doc = json.loads(f.read())
		if debug:
			print(json.dumps(doc, indent=4, sort_keys=True))
		f.close()
		routes = []
		for route in doc['routes']:
			routes.append((route['name'],float(route['time'])/60.0))
		return routes
	except Exception as ex: 
		print(ex)
		return None
