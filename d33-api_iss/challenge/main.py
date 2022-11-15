import requests
from datetime import datetime
import smtplib
from dotenv import dotenv_values
import time 

config = dotenv_values("../../.env")
MAIL_NAME = config['MAIL_NAME']
MAIL_PASS = config['MAIL_PASS']
MY_LAT = 48.856613 
MY_LONG = 2.352222 

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now().hour

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

print ("time:",time_now)

def send_email():
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MAIL_NAME, password=MAIL_PASS)
        connection.sendmail(from_addr=MAIL_NAME, to_addrs="rom.chenard@gmail.com",
                            msg=f"subject:Look up and Watch ISS !\n\n super !")

while True:
    if time_now>sunset and time_now<sunrise :
        if abs(iss_latitude-MY_LAT)<=5:
            if abs(iss_longitude-MY_LONG)<=5:
                send_email()
            else:
                print('not thee right longitude')
        else:
            print("not the right lattitude")
    else:
        print("not dark")
    time.sleep(60)

