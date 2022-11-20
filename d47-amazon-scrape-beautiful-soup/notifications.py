import dotenv
import smtplib
config = dotenv.dotenv_values()

MAIL_NAME = config['MAIL_NAME']
MAIL_PASS = config['MAIL_PASS']

class NotificationManager:
    def __init__(self) -> None:
        self.mail = "rom.chenard@gmail.com"

    def send_emails(self, url, price):
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=MAIL_NAME, password=MAIL_PASS)
            connection.sendmail(from_addr=MAIL_NAME, to_addrs=self.mail,
                                msg=f"subject:Motivation quote\n\n new Price : {price} for : {url}")
                