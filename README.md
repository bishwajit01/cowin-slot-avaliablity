# Read Me

### APIs used for coWin-availablity-slot project
Reference from :
    https://apisetu.gov.in/public/marketplace/api/cowin

## Metadata APIs
| HTTP Method | API Endpoint | DESCRIPTION |
| ------ | ------ | ------ |
| GET | /v2/admin/location/states | API to get all the states in India |
| GET | /v2/admin/location/district/{state_id} | API to get all the states in India |

## Appointment Availability APIs
| HTTP Method | API Endpoint| Query Parameter|DESCRIPTION |
| ------ | ------ | ------ | ------ |
|GET | /v2/appointment/sessions/public/findByPin | eg. pincode= 560100, date = 30-06-2021, date format[DD-MM-YYYY] and should be T+1 |Get the appointment availablity by using the pincode|
|GET | /v2/appointment/sessions/public/findByDistrict | eg. district_id= 276, date = 30-06-2021, date format[DD-MM-YYYY] and should be T+1 |Get the appointment availablity by using the pincode|


# Creating a Telegram Bot and Publishing to the channel
---------------------------------------------------------------

## Creating the Bot
* Search for BotFather in Telegram with the bluetick
* Type /newbot
* It will ask to give a aliasname for the bot
* Give the bot name(it should end with _bot at the end, Example: bruce_bot)
* We will get a message from BotFather with a token in it.
* Save the token some where safe.
* Hit the url :: https://api.telegram.org/bot<tokenId>/getupdates

## Adding a bot to the Channel
* Create a channel in Telegram
* Add bot(@bruce_bot) to the channel and make it admin with the desired admin rights.
* Again hit the same url :: https://api.telegram.org/bot<tokenId>/getupdates
* From the response you will get the chat id and channel name.
* Save it somewhere safe.


## Sending Message to the channnel using the bot
* With the saved token-id and chat-id you can send the message to the channel
    * Example :: https://api.telegram.org/bot' + TOKEN_ID + '/sendMessage?chat_id=' + chat_id + '&parse_mode=MarkdownV2&text=' + message
    * you can replace the message with your custom message.
    * Final URL :: https://api.telegram.org/botXXXXXXX/sendMessage?chat_id=XXXXX&parse_mode=MarkdownV2&text=Hi

