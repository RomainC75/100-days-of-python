import requests
from bs4 import BeautifulSoup
import lxml

url = "https://www.empireonline.com/movies/features/best-movies-2"

raw_ans = requests.get(url)
raw_ans.raise_for_status()

# the page I got with requests is different from Firefox
# no H3 !!

soup = BeautifulSoup(raw_ans.content, 'html.parser')

movies = soup.find_all(name="div", class_="listicle-item")
ranking = [ movie.find(name="img").get("alt") for movie in movies ]
ranking.reverse()

for i,movie in enumerate(ranking):
    print(f'{i+1} : {movie}')
