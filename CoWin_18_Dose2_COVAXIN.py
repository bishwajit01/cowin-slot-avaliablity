import re
import json

def send18D2CovaxinMessages(items, dateToBeprinted):
    item = json.loads(items)
    min_age = item['min_age_limit']
    doseCapacity = item['available_capacity_dose2']

    address = item['address']
    address = re.sub('[.]', ' ', address)
    address = re.sub('[-]', ' ', address)
    address = re.sub('[)]', ' ', address)
    address = re.sub('[(]', ' ', address)

    name = item['name']
    name = re.sub('[.]', ' ', name)
    name = re.sub('[-]', ' ', name)
    name = re.sub('[)]', ' ', name)
    name = re.sub('[(]', ' ', name)

    if min_age == 18 and doseCapacity > 0 :
        message = 'Age Group: 18 to 44' + '\n'
        message = message + name + '\n' + address + '\n'
        message = message + 'Pincode: ' + str(item['pincode']) + '\n'
        message = message + 'Vaccine: ' + item['vaccine'] + '\n'
        message = message + 'FeeType: ' + item['fee_type'] + '\n'
        message = message + 'DATE: ' + dateToBeprinted + '\n'
        message = message + 'Dose1: ' + str(item['available_capacity_dose1']) + '\n'
        message = message + 'Dose2: ' + str(item['available_capacity_dose2']) + '\n'
        print(message)
        if doseCapacity > 1 and item['vaccine'] == 'COVAXIN':
            return message