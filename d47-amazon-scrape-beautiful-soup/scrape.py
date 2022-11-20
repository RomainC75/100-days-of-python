import pandas
import requests
import lxml
from bs4 import BeautifulSoup

class Scrape:
    def __init__(self, file_name) -> None:
        self.file_name=file_name
        self.df=None
        self.articles=None
        self.headers={
            "Accept-Language":"en-US,en;q=0.5",
            "User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:107.0) Gecko/20100101 Firefox/107.0"
        }
        self.results=[]

    def import_data_frame(self):
        self.df = pandas.read_csv(self.file_name)
        self.articles = self.df.to_dict(orient= "records")

    def get_price(self,url):
        try:
            ans=requests.get(url=url, headers=self.headers)
            soup = BeautifulSoup(ans.content,'lxml')
            price = soup.select_one(".priceToPay > span")
            print("price : ", price)
            price_text = price.contents[0]
            float_price = float( price_text.replace(",",".").replace("€","") )
            return float_price
        except:
            return None

    def scrape_all(self):
        # print("dict : ", self.dict)
        for article in self.articles:
            price = self.get_price(article['url'])
            print("article : ",article)
            if( price and price<float( article['price'] ) ):
                self.results.append({
                    'url':article['url'],
                    'price':price
                })
        print(self.results)
        return self.results