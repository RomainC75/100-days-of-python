import requests
import dotenv
import smtplib
config = dotenv.dotenv_values()
from twilio.rest import Client
from flight_data import FlightData

MAIL_NAME = config['MAIL_NAME']
MAIL_PASS = config['MAIL_PASS']

class NotificationManager:
    def __init__(self, flightData:FlightData) -> None:
        self.flightData = flightData
        self.data = self.flightData.get_data()
        self.url = 
        self.message = f"Low price alert : {self.data['price']} EUR to fly from {self.data['origin_city']} to {self.data['destination_city']} from {self.data['out_date']} to {self.data['return_date']}. {self.data['stop_overs'] if self.data['stop_overs']>0 else 'no'} {'stops in' if self.data['stop_overs']>0 else ''} {self.data['via_city'] if len(self.data['via_city'])>0 else ''}"
        self.sheety_url="https://api.sheety.co/6a5c5ac0fcac8b7574d0f2b93b8f2e29/flightDestination/users"
        self.sheety_headers = {
            "Authorization":f'Bearer {config["SHEETY_BEARER"]}'
        }

    def send_message(self):
        message = "super ! "
        account_sid = config['TWILIO_ACCOUNT_SID']
        auth_token = config['TWILIO_AUTH_TOKEN']
        client = Client(account_sid, auth_token)
        message = client.messages \
                        .create(
                            body=self.message,
                            from_='+19458004166',
                            to='+33689947378'
                        )
        print(message.status)

    def get_emails(self):
        raw_ans=requests.get(self.sheety_url, headers=self.sheety_headers)
        ans = raw_ans.json()
        return ans

    def send_emails(self):
        for user in self.get_emails()['users']:
            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                connection.starttls()
                connection.login(user=MAIL_NAME, password=MAIL_PASS)
                connection.sendmail(from_addr=MAIL_NAME, to_addrs=user['email'],
                                    msg=f"subject:Motivation quote\n\n {self.message} : click <a href={self.data['link']}>here</a>")

            # MIMEText(u'<a href="www.google.com">abc</a>','html')