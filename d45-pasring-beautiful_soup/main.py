from bs4 import BeautifulSoup
import requests

url = "https://news.ycombinator.com/news"
raw_ans = requests.get(url)
raw_ans.raise_for_status()
data = raw_ans.content

soup = BeautifulSoup(data)
# for title in soup.select("td.title:not([valign])"):
#     print("++++ ", title.select_one('a').contents[0])
#     print("=> ", title.select_one('a').get("href"))

result = []

for line in soup.select("tr[id]"):
    try:
        link=line.select_one("td:nth-child(3) a").get("href")
    except:
        continue
    else:
        rank = line.select_one("span").text
        tag=""
        text=line.select_one("td:nth-child(3)").text
        link=line.select_one("td:nth-child(3) a").get("href")
        try:
            upvote_link=line.select_one("td.votelinks a").get("href")
        except:
            upvote_link=""
        print("upvote : ", upvote_link)
        result.append({
            "rank":rank,
            "text":text,
            "link":link,
            "upvote_link":upvote_link
        })

points = [ int(tag.getText().split(" ")[0]) for tag in soup.find_all(name="span", class_="score") ]

srt = sorted(points)
best = srt[-1]
print("best : ", best)
print("index : ", points.index(best)+1)
print(result[points.index(best)+1])


