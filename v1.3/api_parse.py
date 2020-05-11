#!/usr/bin/env python

import requests
from datetime import datetime
from credentials import TOKEN_ADVERTISER as TOKEN

FORMAT = 'json'
now = datetime.now()
DATA = now.strftime("%d/%m/%Y %H:%M:%S")


def get_ecpm_data(country, carrier):



	url = f'https://www.trafficcompany.com/feed/ivr-carrier-performance?access-token={TOKEN}&format={FORMAT}'
	myobj = {'somekey': 'somevalue'}
	x = requests.get(url, data = myobj)
	data = x.json()
	

	for i in data:
		if i['country_name'] == country and i['carrier_name'] == carrier:
			current_ecpm = i['ecpm_24h']
			
			ecpma = str(current_ecpm)
			
			

	with open('log', 'a') as the_file:
		the_file.write(f'[{DATA}] Checking eCPM for {country} in {carrier}: {ecpma} ... Done 100%\n')

	return ecpma




