import json
import requests
import time
import datetime
import os
import re
import urllib

today_date = datetime.date.today()
today_date = today_date + datetime.timedelta(days=1)
new_today_date = today_date.strftime("%d-%m-%Y")
new_today_date2 = today_date.strftime("%d/%m/%Y")

header_dict = {"Accept-Language": "hi_IN", "Accept-Encoding":"gzip, deflate, br", "Accept":"*/*", "Connection":"keep-alive", "content-type":"application/json; charset=utf-8", "User-Agent": "PostmanRuntime/7.28.0"}
BASE_URL = 'https://cdn-api.co-vin.in/api/'
URL_STATES = 'v2/admin/location/states'
URL_DISTRICTS = 'v2/admin/location/districts/'
URL_FIND_BY_PIN = 'v2/appointment/sessions/public/findByPin'
URL_FIND_BY_DISTRICT = 'v2/appointment/sessions/public/findByDistrict'


def sendMessage(message):
    message = urllib.parse.quote(message, safe='')
    print(message)
    # message = re.sub('[:]+', '\:', message)
    # message = re.sub('[ ]+', '\ ', message)
    # message = re.sub('[.]+', '\.', message)
    chat_id = 'XXXX'
    token_id = 'XXXXXXX'
    send_text = 'https://api.telegram.org/bot' + token_id + '/sendMessage?chat_id=' + chat_id + \
        '&parse_mode=MarkdownV2&text=' + message
    # print("URL >> ", send_text)
    response = requests.get(send_text)
    if response.status_code != 200:
        os.system('say "EXCEPTION"')
    print(response.status_code)
    print(response.json())
    return response.json()


def sendMessages(item):
    min_age = item['min_age_limit']
    doseCapacity = item['available_capacity_dose1']

    address = item['address']
    name = item['name']

    if min_age == 18 and doseCapacity != 0 :
        # print('----------------URBAN------------------')
        # print(item['pincode'], ' ' , item['available_capacity'])
        message = 'Age Group: 18 to 44' + '\n'
        message = message + name + '\n' + address + '\n'
        message = message + 'Pincode: ' + str(item['pincode']) + '\n'
        message = message + 'Vaccine: ' + item['vaccine'] + '\n'
        message = message + 'FeeType: ' + item['fee_type'] + '\n'
        message = message + 'DATE: ' + new_today_date2 + '\n'
        message = message + 'Dose1: ' + str(item['available_capacity_dose1']) + '\n'
        message = message + 'Dose2: ' + str(item['available_capacity_dose2']) + '\n'
        # message = message + "By-Bishwajit Vikram"

        print(message)
        sendMessage(message)

    # if min_age == 45 and doseCapacity != 0 :
    #     message = 'Age Group: 45\+' + '\n'
    #     message = message + item['name'] + '\n' + re.sub('[.]', ' ', address) + '\n'
    #     message = message + 'Pincode: ' + str(item['pincode']) + '\n'
    #     message = message + 'Vaccine: ' + item['vaccine'] + '\n'
    #     message = message + 'FeeType: ' + item['fee_type'] + '\n'
    #     message = message + 'DATE: ' + new_today_date2 + '\n'
    #     message = message + 'Dose1: ' + str(item['available_capacity_dose1']) + '\n'
    #     message = message + 'Dose2: ' + str(item['available_capacity_dose2']) + '\n'
    #     # message = message + "Bishwajit Vikram"

    #     print(message)
    #     sendMessage(message)

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
                                    sendMessages(item)
                                    # min_age = item['min_age_limit']
                                    # doseCapacity = item['available_capacity']
                                    # if min_age < 40 and doseCapacity != 0 :
                                    #     print('----------------URBAN------------------')
                                    #     print(item['pincode'], ' ' , item['available_capacity'])
                                    #     message = str(item['pincode']) + '\nSlots:' + str(item['available_capacity_dose1']) + '\n' + 'Address\:' + str(item['address'])
                                    #     print(message)
                                    #     # sendMessage(message)
                                    #     sendMessages(item)
                                    #     os.system('say "Book it fast!!!!!!!!"')
                            if districtName.find("Bangalore Rural") == 0:
                                # print(districtName)
                                queryParam = '?district_id=' + str(item['district_id']) + '&date=' + new_today_date
                                response = requests.get(BASE_URL + URL_FIND_BY_DISTRICT + queryParam, headers=header_dict)
                                sessions = response.json()['sessions']
                                for item in sessions:
                                    sendMessages(item)
                                    # min_age = item['min_age_limit']
                                    # doseCapacity = item['available_capacity_dose1']
                                    # if min_age < 40 and doseCapacity != 0:
                                    #     print('---------------RURAL-----------------')
                                    #     print(item['pincode'], ' ' , item['available_capacity_dose1'])
                                    #     message = str(item['pincode']) + '\nSlots:' + str(item['available_capacity_dose1']) + '\n' + 'Address\:' + str(item['address'])
                                    #     print(message)
                                    #     # sendMessage(message)
                                    #     sendMessages(item)
                                    #     os.system('say "Book it fast!!!!!!!!"')
                            if districtName.find("BBMP") == 0:
                                # print(districtName)
                                queryParam = '?district_id=' + str(item['district_id']) + '&date=' + new_today_date
                                response = requests.get(BASE_URL + URL_FIND_BY_DISTRICT + queryParam, headers=header_dict)
                                sessions = response.json()['sessions']
                                for item in sessions:
                                    sendMessages(item)
                                    # min_age = item['min_age_limit']
                                    # doseCapacity = item['available_capacity_dose1']
                                    # if min_age < 40 and doseCapacity != 0:
                                    #     print('---------------BBMP-----------------')
                                    #     print(item['pincode'], ' ' , item['available_capacity_dose1'])
                                    #     message = str(item['pincode']) + '\nSlots:' + str(item['available_capacity_dose1']) + '\n' + 'Address\:' + str(item['address'])
                                    #     print(message)
                                    #     # sendMessage(message)
                                    #     sendMessages(item)
                                    #     os.system('say "Book it fast!!!!!!!!"')
        count = count + 1
        time.sleep(10)
    except Exception as e:
        print("An exception occurred..sleeping for 15 sec")
        print(e)
        count = count + 1
        time.sleep(15)
