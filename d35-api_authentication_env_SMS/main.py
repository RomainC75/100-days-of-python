import requests
import dotenv
config = dotenv.dotenv_values('../.env')
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

#start 7am
# check next 12h
#send sms if rain

proxy_client = TwilioHttpClient()
proxy_client.session.proxies = {'https': os.environ['https_proxy']}

MY_LAT = 48.856613 
MY_LONG = 2.352222 

params ={
    "lat":MY_LAT,
    "lon":MY_LONG,
    "appid":config['OPENWEATHER_KEY'],
    "exclude":"current,minutely,daily"
}

raw = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=params)
raw.raise_for_status()
weather_data = raw.json()

def send_sms():
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token, http_client=proxy_client)

    message = client.messages \
                    .create(
                        body="Bring an Umbrella - from Carotte and Python :-)",
                        from_='+19458004166',
                        to='+33682187627'
                    )

    print(message.status)

will_rain = False

for dt in weather_data['hourly'][:12]:
    if(dt['weather'][0]['id']<700):
        print("rain") 
        will_rain=True
        break

if will_rain:
    send_sms()
