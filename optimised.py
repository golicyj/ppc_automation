#!/usr/bin/env python

import requests

# set api keys: affiliate, advertising and telegram APIs

aff_key = ''
ad_key = ''
tg_key = ''
chat_id = ''

# set campaign id
cuba = 3193880
argentina = 3223798
peru = 3227946

# set eCPM parameters
ecpm_max = 40
ecpm_min = 40

# set list of country to check
list = ['Cuba', 'Argentina', 'Peru']


url = 'https://www.your-aff-network.com/feed/your-json?access-token=' +aff_key+ '&format=json'
x = requests.get(url)
data = x.json()


def camp_start(camp, status): # 'status' = play/stop
    if camp == 'Cuba': camp == cuba
    if camp == 'Argentina': camp == argentina
    if camp == 'Peru': camp == peru

    headers = {
        'accept': 'application/json',
        'Authorization': ad_key,
        'Content-Type': 'application/json',
    }

    data = '{"campaign_ids":[' + str(cuba) + ']}'
    response = requests.put('https://ssp-api.your-ad-network.com/v5/adv/campaigns/' + status + '', headers=headers, data=data)
    #print(response, status)


def telegram_alert(message):
    url = 'https://api.telegram.org/'+tg_key+'/sendMessage?chat_id='+ chat_id +'&text='+ message +''
    x = requests.post(url)


def find_best_veticals(geo_name):

    try:
        for i in data:
            if i['ecpm_24h'] > ecpm_max and i['country_name'] == geo_name:
                camp_start(geo_name, 'play')
                a = '' +geo_name + ' is START now. ECPM:' + str(i['ecpm_24h']) + ' USD'
                telegram_alert(a)
                break

            if i['ecpm_24h'] < ecpm_min and i['country_name'] == geo_name:
                camp_start(geo_name, 'stop')
                a = '' +geo_name + ' is STOP now. ECPM:' + str(round(i['ecpm_24h'],1)) + ' USD'
                telegram_alert(a)
                break
    except:
        print('No profitable country found')


for x in list:
    find_best_veticals(x)
