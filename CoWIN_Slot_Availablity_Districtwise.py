import json
import requests
import time
import datetime
import os

today_date = datetime.date.today()
today_date = today_date + datetime.timedelta(days=1)
new_today_date = today_date.strftime("%d-%m-%Y")

header_dict = {"Accept-Language": "hi_IN", "Accept-Encoding":"gzip, deflate, br", "Accept":"*/*", "Connection":"keep-alive", "content-type":"application/json; charset=utf-8", "User-Agent": "PostmanRuntime/7.28.0"}
BASE_URL = 'https://cdn-api.co-vin.in/api/'
URL_STATES = 'v2/admin/location/states'
URL_DISTRICTS = 'v2/admin/location/districts/'
URL_FIND_BY_PIN = 'v2/appointment/sessions/public/findByPin'
URL_FIND_BY_DISTRICT = 'v2/appointment/sessions/public/findByDistrict'

count = 0
while True:
    try:
        print('counter :: ', count)
        response = requests.get(BASE_URL + URL_STATES, headers=header_dict)
        response.status_code = 200
        if response.status_code == 200:
            # print(response.content)
            states = response.json()['states']
            # print(states)
            for item in states:
                if item['state_name'] == 'Karnataka':
                    stateId = str(item['state_id'])
                    response = requests.get(BASE_URL + URL_DISTRICTS + stateId, headers=header_dict)
                    # print(response.status_code)
                    if response.status_code == 200:
                        districts = response.json()['districts']
                        # print(districts)
                        for item in districts:
                            districtName = item['district_name']
                            # print(type(districtName))
                            if districtName.find("Bangalore Urban") == 0:
                                # print(districtName)
                                queryParam = '?district_id=' + str(item['district_id']) + '&date=' + new_today_date
                                response = requests.get(BASE_URL + URL_FIND_BY_DISTRICT + queryParam, headers=header_dict)
                                sessions = response.json()['sessions']
                                for item in sessions:
                                    min_age = item['min_age_limit']
                                    doseCapacity = item['available_capacity']
                                    if min_age < 40 and doseCapacity != 0 :
                                        print('----------------URBAN------------------')
                                        print(item['pincode'], ' ' , item['available_capacity'])
                                        os.system('say "Slot Available. Book it fast!!!!!!!!"')
                            if districtName.find("Bangalore Rural") == 0:
                                # print(districtName)
                                queryParam = '?district_id=' + str(item['district_id']) + '&date=' + new_today_date
                                response = requests.get(BASE_URL + URL_FIND_BY_DISTRICT + queryParam, headers=header_dict)
                                sessions = response.json()['sessions']
                                for item in sessions:
                                    min_age = item['min_age_limit']
                                    doseCapacity = item['available_capacity_dose1']
                                    if min_age < 40 and doseCapacity != 0:
                                        print('---------------RURAL-----------------')
                                        print(item['pincode'], ' ' , item['available_capacity_dose1'])
                                        os.system('say "Slot Available. Book it fast!!!!!!!!"')
                            if districtName.find("BBMP") == 0:
                                # print(districtName)
                                queryParam = '?district_id=' + str(item['district_id']) + '&date=' + new_today_date
                                response = requests.get(BASE_URL + URL_FIND_BY_DISTRICT + queryParam, headers=header_dict)
                                sessions = response.json()['sessions']
                                for item in sessions:
                                    min_age = item['min_age_limit']
                                    doseCapacity = item['available_capacity_dose1']
                                    if min_age < 40 and doseCapacity != 0:
                                        print('---------------BBMP-----------------')
                                        print(item['pincode'], ' ' , item['available_capacity_dose1'])
                                        os.system('say "Slot Available. Book it fast!!!!!!!!"')
        count = count + 1
        time.sleep(5)
    except:
        print("An exception occurred..sleeping for 15 sec")
        count = count + 1
        time.sleep(15)