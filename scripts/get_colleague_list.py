import requests
from bs4 import BeautifulSoup
import json

url = "https://szbi-pg.hu/index.php/hu/munkatarsaink"

soup = BeautifulSoup(requests.get(url).content.decode(), features="lxml")

sections = [x for x in soup.find("div", id="agmedia_responsibilities").find("div").findAll("div")]

output = []
for section in sections:
    if section == None:
        continue
    header = section.find("header")
    if header == None:
        continue

    sectionObj = {"title": header.text.strip(), "people": []}

    imgs = section.findAll("img")
    for person, image in zip(section.findAll("div", class_="profile"), imgs):
        personJson = {
            "name": person.find("h1").text.strip(),
            "contact": person.find("div", class_="contact").text.strip(),
            "description": person.find("h2").text.strip().replace("\r", "").split("\n"),
            "img": "https://szbi-pg.hu"+image["src"]
        }

        sectionObj["people"].append(personJson)

    output.append(sectionObj)

print(json.dumps(output, ensure_ascii=False))
