import re
import pandas  as pd
from geopy import geocoders
import geocoder
import time

def user():
	user = pd.read_csv('./us user.csv')
	print(user.columns)
	LST = []
	for k, v in user.groupby('a.city_name'):
		LST.append(k)

def geolist():
	GEO_LIST = []
	pattern = '[0-9]'
	for i in LST:
		i = re.sub(pattern, '', i)
		i = i.replace(",", "")
		i = i.lstrip()
		GEO_LIST.append(i)
	GEO_LIST[:] = [item for item in GEO_LIST if item != '']

def geoid(GEO_LIST):
	A = []
	B = []
	for i in GEO_LIST:
		g = geocoder.geonames(i, key = 'kevinshi')
		A.append(i)
		B.append(g.geonames_id)
		print(i)
		print(g.geonames_id)

	GEO_NAME = pd.DataFrame(
	    {'City': A,
	     'Geo_id': B
	    })

	GEO_NAME.to_excel('./list_name.xlsx', index =False)

nonempty = pd.read_excel('./nonempty.xlsx')
exist = pd.read_excel('./exist.xlsx')
nonempty = nonempty['geo_id'].tolist()
exist = exist['Geo ID'].tolist()
GEO_LIST = list(set(nonempty) - set(exist))
print("length:",len(GEO_LIST))

def db(GEO_LIST):
	#Para:
	GEO_ID = []
	LAT = []
	LOG = []
	COUNTRY = []
	STATE = []
	TIMEZONE = []
	for i in GEO_LIST:
		try:
			i = int(i)
			GEO_ID.append(i)
			g = geocoder.geonames(i, method='details', key= 'jeffzhong')
			LAT.append(g.lat)
			LOG.append(g.lng)
			COUNTRY.append(g.country)
			STATE.append(g.state)
			TIMEZONE.append(g.timeZoneName) 
			print(i)
			print(g.lat)
			print(g.lng)
			print(g.country)
			print(g.state)
			print(g.timeZoneName)
		except:
			continue

	DB = pd.DataFrame(
	    {'Geo ID': GEO_ID,
    	 'Latitude': LAT,
	     'Logtitude': LOG,
	     'Country': COUNTRY,
	     'State': STATE,
	     'Timezone': TIMEZONE
	    })
	print(DB)

# geoid(GEO_LIST)
db(GEO_LIST)
