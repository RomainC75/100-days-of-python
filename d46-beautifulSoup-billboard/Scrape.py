import requests
from bs4 import BeautifulSoup
import lxml

class Scrape:
    def __init__(self) -> None:
        self.url="https://www.billboard.com/charts/hot-100"

    def get_top_100(self, date):
        raw_ans = requests.get(f'{self.url}/{date}')
        raw_ans.raise_for_status()
        soup = BeautifulSoup(raw_ans.content,'lxml')
        list = soup.select(".o-chart-results-list-row-container")
        print( len( list ) )
        top_list = []
        for entry in list:
            title = entry.select_one("h3").contents[0].strip()
            artist = entry.select_one(" ul > li:nth-child(4) > ul > li:nth-child(1) > span").contents[0].strip()
            top_list.append({
                "title":title,
                "artist":artist
            })
        return top_list