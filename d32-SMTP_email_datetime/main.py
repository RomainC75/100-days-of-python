import smtplib
from dotenv import dotenv_values
import random 

config = dotenv_values("../.env")
MAIL_NAME = config['MAIL_NAME']
MAIL_PASS = config['MAIL_PASS']

print(MAIL_NAME, MAIL_PASS)
# connection = smtplib.SMTP("smtp.gmail.com", 587)
# connection.starttls()
# connection.login(user=MAIL_NAME,password=MAIL_PASS)
# connection.sendmail(from_addr=MAIL_NAME, to_addrs="rom.chenard@gmail.com", msg="subject:Hello\n\nMy email body")
# connection.close()

# close connection automatically
def send_mail(quote):
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MAIL_NAME, password=MAIL_PASS)
        connection.sendmail(from_addr=MAIL_NAME, to_addrs="rom.chenard@gmail.com",
                            msg=f"subject:Motivation quote\n\n {quote}")

def get_random_quote():
    try:
        file = open("./quotes.txt","r")
    except FileNotFoundError:
        print("=>Error ! file not found !")
        quote = input("write you personnal quote : ")
    else:
        quotes = file.readlines()
        quote = random.choice(quotes)
    return quote

import datetime as dt

now = dt.datetime.now()
year=now.year
month=now.month
day_of_week=now.weekday()

date_of_birth = dt.datetime(year=1985,month=12,day=25, hour=4)
print(date_of_birth, day_of_week)

if day_of_week==1:
    quote = get_random_quote()
    send_mail(quote)
else:
    print("not the good day for this")
