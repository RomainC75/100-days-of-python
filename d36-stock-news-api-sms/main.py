import requests
import dotenv
config = dotenv.dotenv_values("../.env")
import re
import datetime as dt
import os
from twilio.rest import Client


def get_last_value_end_of_day(data):
    values=[]
    for key in data['Time Series (60min)'].keys():
        last_closing_time=re.search(r'(\d{2}):\d{2}:\d{2}',key)
        if(last_closing_time.group(1)=='20'):
            values.append(data['Time Series (60min)'][key]["1. open"])
    return values

def send_sms(delta,message):
    account_sid = config['TWILIO_ACCOUNT_SID']
    auth_token = config['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)
    message = client.messages \
                    .create(
                        body=f'delta : {delta}\n{message}',
                        from_='+19458004166',
                        to='+33689947378'
                    )
    print(message.status)

def concat_titles(selected_news):
    if len(selected_news)>=3:
        max=3
    else:
        max=len(selected_news)
    titles=[new['title'] for new in selected_news[:max]]
    return "\n========\n".join(titles)


def get_news(name):
    yesterday = dt.date.today()- dt.timedelta(days=1)
    yesterdate=f"{yesterday.year}-{yesterday.month}-{yesterday.day}"
    news_url="https://newsapi.org/v2/everything"
    NEWS_KEY=config['NEWSAPI_KEY']
    news_params={
        "q":name,
        "from":yesterdate,
        "sortBy":"publishedAt",
        "apikey":NEWS_KEY
    }
    news_raw = requests.get(news_url,params=news_params)
    news_raw.raise_for_status()
    news = news_raw.json()
    return news



finance_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=TSLA&interval=60min&apikey={config['ALPHA_ADVANTAGE_KEY']}"
raw = requests.get(finance_url)
raw.raise_for_status()
stock_data = raw.json()
values = get_last_value_end_of_day(stock_data)

evolution = []

# get an array of the evolution up the last "ends of the day" (20:00)
for i,v in enumerate(values[:-1]):
    pourcent = float(v)/float(values[i+1])*100-100
    small="{:.2f}".format(pourcent)
    evolution.append(small)

# if there is a difference of at least 5% between the 2 last closing hours
# send a message with with the 3 first titles found
if abs(float(evolution[0]))>=5:
    news=get_news("Tesla")
    selected=[]
    for article in news['articles']:
        if re.search(r'.\.com|\.fr.',article['url']):
            if re.search(r'million|billion',article['title']):
                selected.append(article)
    send_sms(evolution[0],concat_titles(selected))