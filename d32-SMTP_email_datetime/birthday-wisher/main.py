##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
import datetime as dt
import pandas as pd
import random
import smtplib
from dotenv import dotenv_values
config = dotenv_values("../../.env")

MAIL_NAME = config['MAIL_NAME']
MAIL_PASS = config['MAIL_PASS']
TEMPLATES_PATH = "./letter_templates"
print(MAIL_NAME,MAIL_PASS)

now = dt.datetime.now()
today_day=now.day
today_month=now.month

# the program has to stop anyway
# so, the try/except is not the best thing to do
try:
    df = pd.read_csv("./birthdays.csv")
except :
    print("fill the birthay.csv file !")
    exit()

birthdays_data = df.to_dict(orient="records")

def get_today_birthday_names():
    names=[]
    for person in birthdays_data:
        if person['day']==today_day and person['month']==today_month:
            names.append(person)
    return names

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
def create_new_letter_for_a_name(name):
    letter_number=random.randint(1,3)
    try:
        file = open(f'{TEMPLATES_PATH}/letter_{letter_number}.txt')
    except FileNotFoundError:
        letter_content="Hey [NAME], happy birthday !"
    else:
        letter_content=file.read()
    letter_content = letter_content.replace("[NAME]", name)
    return letter_content

# 4. Send the letter generated in step 3 to that person's email address.

def send_mail(letter_content, mail):
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MAIL_NAME, password=MAIL_PASS)
        connection.sendmail(from_addr=MAIL_NAME, to_addrs="rom.chenard@gmail.com",
                            msg=f"subject:Motivation quote\n\n {letter_content}")


target_names = get_today_birthday_names()
if len(target_names)>0:
    for name_infos in target_names:
        letter_content=create_new_letter_for_a_name(name_infos['name'])
        send_mail(letter_content,name_infos["email"])
else:
    print("nothing to do today :-)")