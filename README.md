# Read Me

### APIs used for coWin-availablity-slot project
Reference taken from :
    https://apisetu.gov.in/public/marketplace/api/cowin

## Metadata APIs
| HTTP Method | API Endpoint | DESCRIPTION |
| ------ | ------ | ------ |
| GET | /v2/admin/location/states | API to get all the states in India |
| GET | /v2/admin/location/district/{state_id} | API to get all the states in India |

## Appointment Availability APIs
| HTTP Method | API Endpoint| Query Parameter|DESCRIPTION |
| ------ | ------ | ------ | ------ |
|GET | /v2/appointment/sessions/public/findByPin | eg. pincode= 560100, date = 30-06-2021, date format[DD-MM-YYYY] and should be  should be T+1 |Get the appointment availablity by using the pincode|
|GET | /v2/appointment/sessions/public/findByDistrict | eg. district_id= 560100, date = 30-06-2021, date format[DD-MM-YYYY] and should be  should be T+1 |Get the appointment availablity by using the pincode|
|GET | /v2/appointment/sessions/public/findByPin | eg. pincode= 560100, date = 30-06-2021, date format[DD-MM-YYYY] and should be  should be T+1 |Get the appointment availablity by using the pincode|
