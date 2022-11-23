import smtplib
from dotenv import dotenv_values
import random 

config = dotenv_values("../../.env")



# connection = smtplib.SMTP("smtp.gmail.com", 587)
# connection.starttls()
# connection.login(user=MAIL_NAME,password=MAIL_PASS)
# connection.sendmail(from_addr=MAIL_NAME, to_addrs="rom.chenard@gmail.com", msg="subject:Hello\n\nMy email body")
# connection.close()

# close connection automatically


class MailHandler:
    def __init__(self) -> None:
        self.MAIL_NAME = config['MAIL_NAME']
        self.MAIL_PASS = config['MAIL_PASS']

    def craft_email(self, form_data):
        print("inside : ", form_data)
        str=f"New data received : \n name : {form_data['name']} \n mail : {form_data['email']} \n phone : {form_data['phone']} \n message : {form_data['message']}"
        # str=f'New data received : {form_data[0][1]},{form_data[1][1]},{form_data[2][1]},{form_data[3][1]}'
        return str

    def send_mail(self, quote):
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=self.MAIL_NAME, password=self.MAIL_PASS)
            connection.sendmail(from_addr=self.MAIL_NAME, to_addrs="rom.chenard@gmail.com",
                msg=f"subject:New Contact\n\n {quote}")
    