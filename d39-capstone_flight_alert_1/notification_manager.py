import dotenv
config = dotenv.dotenv_values()
from twilio.rest import Client
from flight_data import FlightData

class NotificationManager:
    def __init__(self, flightData:FlightData) -> None:
        self.flightData = flightData

    def send_message(self):
        data = self.flightData.get_data()
        message = "super ! "
        account_sid = config['TWILIO_ACCOUNT_SID']
        auth_token = config['TWILIO_AUTH_TOKEN']
        client = Client(account_sid, auth_token)
        message = client.messages \
                        .create(
                            body=f"Low price alert : {data['price']} to fly from {data['origin_city']} to {data['destination_city']} from {data['out_date']} to {data['return_date']}",
                            from_='+19458004166',
                            to='+33689947378'
                        )
        print(message.status)