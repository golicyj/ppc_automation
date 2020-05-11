#!/usr/bin/env python

import requests
import api_parse
from datetime import datetime
from campaing_manager import campaign_manage as campaign


geo_actual = {}
geo_to_work = []
geo_to_stop = []
ECPM_TARGET = 20		
geo_list = {'Cuba':'ETECSA', 
			'Peru':'Entel', 
			'Argentina':'Claro'
			}


class Optimize():

	''' Klasa złuży do optymalizacji dowolnej kampani
	na zasadzie podania kraju oraz operatora'''

	def ecpm_check(self): # sprawdzamy ecpm dla wskazanych krajów

		for key, value in geo_list.items(): 
			geo_actual.update( { key : api_parse.get_ecpm_data(key, value) } )


	def ecpm_find(self):  #zostawiamy tylko te kraje, które pasują
		for key, value in geo_actual.items():
			value = float(value)
			if value > ECPM_TARGET:
				geo_to_work.append(key)
			else:
				geo_to_stop.append(key)
			

	def manage_camp(self): #puszczamy wybrane kampanii
		for var in geo_to_work:
			campaign(f'{var}', 'play')

	def manage_camp_stop(self): #puszczamy wybrane kampanii
		for var in geo_to_stop:
			campaign(f'{var}', 'stop')


a = Optimize()
a.ecpm_check()
a.ecpm_find()
a.manage_camp()
a.manage_camp_stop()
