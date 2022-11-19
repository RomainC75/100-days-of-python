from bs4 import BeautifulSoup
import lxml

with open("website.html","r") as file:
    content = file.read()
    print("content : " , content)

# soup = BeautifulSoup(content, 'html.parser')
soup = BeautifulSoup(content, 'lxml')

#=========indented print
print(soup.prettify())

#=========get the first found
print(soup.h3)

#=========find every corresponding
all_anchor_tags = soup.find_all(name="a")
for a in all_anchor_tags:
    print("==>",a.getText())
    print(a.get('href'))

#=========find by attribute
heading = soup.find_all(name="h1", id="name")
print("heading",heading)

#=========find with class
section_heading = soup.find(name="h3", class_="heading")
print("section_heading", section_heading.name)
print("section_heading", section_heading.get("class"))

#========CSS selectors======
company_url = soup.select_one(selector="p > em > strong >  a").get("href")
print("conpany_url : ", company_url)

print("==>",soup.find_all("a"))

print("==>",soup.find("input").get("maxlength")  )