
import requests
from bs4 import BeautifulSoup
import lxml
from scrape import Scrape
from notifications import NotificationManager

url="https://www.amazon.fr/dp/B004Y6AJP2/ref=syn_sd_onsite_desktop_254?ie=UTF8&psc=1&pd_rd_plhdr=t"


ff_headers={
    "Accept-Language":"en-US,en;q=0.5",
    "User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:107.0) Gecko/20100101 Firefox/107.0"
}

# raw_ans=requests.get(url=url, headers=ff_headers)
# raw_ans.raise_for_status()
# print(raw_ans.content)

# soup = BeautifulSoup(raw_ans.content,'lxml')
# price = soup.select_one(".priceToPay > span")
# price_text = price.contents[0]
# print("price_text : ", price_text)
# float_price = float( price_text.replace(",",".").replace("€","") )
# print("float_price : ", float_price)


notification = NotificationManager()

try:
    file = open('articles.csv',"r")
    file.close()
except FileNotFoundError:
    print("=> articles.csv not found")
else:
    scrape = Scrape("articles.csv")
    scrape.import_data_frame()

    data_to_send = scrape.scrape_all()
    for article in data_to_send:
            notification.send_emails(article['url'], article['price'])
