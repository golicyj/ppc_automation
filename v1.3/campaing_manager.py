#!/usr/bin/env python

import requests
from datetime import datetime
from credentials import TOKEN_PLATFORM as TOKEN
from campaigns_id import *

now = datetime.now()
DATA = now.strftime("%d/%m/%Y %H:%M:%S")


def campaign_manage(idd, state):  #id dla id kampanii, może zawierać 'play' lub 'stop'
	
	for key, value in geo_data.items():
		if key == idd:
			x = value
			headers = {
				'accept':'application/json',
				'Authorization': f'Bearer {TOKEN}',
				'Content-Type': 'application/json'
			}
			data = '{"campaign_ids":[%(x)]}'
			response = requests.put(f'https://ssp-api.propellerads.com/v5/adv/campaigns/{state}', headers=headers, data=data)
			data = response.json()
			with open('log', 'a') as the_file:
				the_file.write(f'[{DATA}] Campaign status for {x}: {state} ... Done 100%\n')

