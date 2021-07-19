import json
import requests
import time
import datetime
import os
import re
import urllib
from CoWin_18_Dose1 import send18D1Messages
from CoWin_45_Dose1 import send45D1Messages
from CoWin_18_Dose2 import send18D2Messages
from CoWin_45_Dose2 import send45D2Messages
from CoWin_45_Dose2_COVIDSHIELD import send45D2CovishieldMessages
from CoWin_18_Dose2_COVAXIN import send18D2CovaxinMessages
from CoWin_18_Dose1_SPUTNIKV import send18D1SPUTNIKVMessages

today_date = datetime.date.today()
today_date = today_date + datetime.timedelta(days=1)
new_today_date = today_date.strftime("%d-%m-%Y")
new_today_date2 = today_date.strftime("%d/%m/%Y")

header_dict = {"User-Agent": "Vikram"}
BASE_URL = 'https://cdn-api.co-vin.in/api/'
URL_STATES = 'v2/admin/location/states'
URL_DISTRICTS = 'v2/admin/location/districts/'
URL_FIND_BY_PIN = 'v2/appointment/sessions/public/findByPin'
URL_FIND_BY_DISTRICT = 'v2/appointment/sessions/public/findByDistrict'
STATE_LIST = [16, 17, 9, 21]
BANGALORE_LIST = [276, 265, 294]
TUMKUR_LIST = [288]
UDUPI_LIST = [286]
ERNAKULAM_LIST = [307]
PUNE_LIST = [363]
DELHI_LIST = [140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150]
DISTRICT_LIST = [276, 265, 294, 286, 307, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 363, 288]
CHAT_ID_BLR18D1 = '-XXXXXX'
CHAT_ID_UDU18D1 = '-XXXXXX'
CHAT_ID_DEL18D1 = 'XXXXXX'
CHAT_ID_ERN45D2_COVIDSHIELD = 'XXXXXX'
CHAT_ID_PUN18D1 = 'XXXXXX'
CHAT_ID_TUM18D1 = 'XXXXXX'
CHAT_ID_DEL18D1_SPUTNIK = 'XXXXXX'
TOKEN_ID = 'XXXXXX'


def sendMessage(message, chat_id):
    if message != None:
        print()
        print(message)
        message = urllib.parse.quote(message, safe='')
        print(message)
        send_textURL = 'https://api.telegram.org/bot' + TOKEN_ID + '/sendMessage?chat_id=' + chat_id + \
            '&parse_mode=MarkdownV2&text=' + message
        print("URL >> ", send_textURL)
        response = requests.get(send_textURL)
        if response.status_code != 200:
            print('Exception :: ', response.json())
            # os.system('say "EXCEPTION"')
            time.sleep(25)
        print(response.status_code)
        print(response.json())
        # time.sleep(25)
        return response.json()
    else:
        # print("-->Send Message is none.",)
        return None

def postMessageToChannels(item, districtId):
    queryParam = '?district_id=' + str(districtId) + '&date=' + new_today_date
    sessionURL = BASE_URL + URL_FIND_BY_DISTRICT + queryParam
    sessionResponse = requests.get(sessionURL, headers=header_dict)
    print('--->sessionResponse = ', sessionResponse.status_code, end='*')
    print('-->districtId = ', districtId, end='*')
    if sessionResponse.status_code == 200:
        sessions = sessionResponse.json()['sessions']
        for item in sessions:
            if districtId in BANGALORE_LIST:
                sendMessage(send18D1Messages(json.dumps(item), str(new_today_date2)), CHAT_ID_BLR18D1)
                time.sleep(1)
            if districtId in UDUPI_LIST:
                sendMessage(send18D1Messages(json.dumps(item), str(new_today_date2)), CHAT_ID_UDU18D1)
                time.sleep(1)
            if districtId in ERNAKULAM_LIST:
                sendMessage(send45D2CovishieldMessages(json.dumps(item), str(new_today_date2)), CHAT_ID_ERN45D2_COVIDSHIELD)
                time.sleep(1)
            if districtId in DELHI_LIST:
                sendMessage(send18D2CovaxinMessages(json.dumps(item), str(new_today_date2)), CHAT_ID_DEL18D2_COVAXIN)
                sendMessage(send18D1Messages(json.dumps(item), str(new_today_date2)), CHAT_ID_DEL18D1)
                sendMessage(send18D1SPUTNIKVMessages(json.dumps(item), str(new_today_date2)), CHAT_ID_DEL18D1_SPUTNIK)
                time.sleep(1)
            if districtId in PUNE_LIST:
                sendMessage(send18D1Messages(json.dumps(item), str(new_today_date2)), CHAT_ID_PUN18D1)
                time.sleep(1)
            if districtId in TUMKUR_LIST:
                sendMessage(send18D1Messages(json.dumps(item), str(new_today_date2)), CHAT_ID_TUM18D1)
                time.sleep(1)
    else:
        print("session Response : ", sessionResponse.status_code)
        return None

def prepareForDistrictURL(stateId):
    districtURL = BASE_URL + URL_DISTRICTS + str(stateId)
    districtResponse = requests.get(districtURL, headers=header_dict)
    print('-->stateId = ', stateId, end='*')
    print('-->districtResponse = ', districtResponse.status_code, end='*')
    if districtResponse.status_code == 200 :
        return districtResponse.json()['districts']
    else :
        print('district Response : ', districtResponse.status_code)
        return None

count = 0
while True:
    print('counter :: ', count, end='')
    try:
        stateURL = BASE_URL + URL_STATES
        stateResponse = requests.get(stateURL, headers=header_dict)
        # print('-->stateResponse = ', stateResponse.status_code, end='')
        if stateResponse.status_code == 200:
            states = stateResponse.json()['states']
            for item in states:
                stateId = item['state_id']
                if stateId in STATE_LIST:
                    districtResponse = prepareForDistrictURL(stateId)
                    if districtResponse != None:
                        for item in districtResponse:
                            districtId = item['district_id']
                            if districtId in DISTRICT_LIST:
                                postMessageToChannels(item, districtId)
        else:
            print('-->stateResponse = ', stateResponse.status_code, end='*')
        count = count + 1
        time.sleep(10)
        print()
    except Exception as e:
        print("An exception occurred for other request..sleeping for 20 sec")
        print(e)
        time.sleep(20)