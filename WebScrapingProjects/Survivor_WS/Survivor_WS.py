from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import pandas as pd


#filename = "Survivor_Cast.csv"
#f = open(filename, "w")
#headers = "cast_name, bio\n"
#f.write(headers)


cast = []
cast.append(["cast_name", "bio", "season"])

for num in range(1, 41):
	survivor_page = 'https://www.cbs.com/shows/survivor/cast/season/' + str(num) + '/'
	# opening up connection, grabbing the page
	uClient = uReq(survivor_page)
	page_html = uClient.read()
	uClient.close()

	# html parser
	page_soup = soup(page_html, "html.parser")

	articles = page_soup.findAll("article",{"class":"grid-view-item"})

	for article in articles:
		articles = page_soup.findAll("article",{"class":"grid-view-item"})
		link = article.a.get("href")

		uClient = uReq('https://www.cbs.com' + link)
		page_html = uClient.read()
		uClient.close()
		page_soup = soup(page_html, "html.parser")

		name = page_soup.find("div", "cast-title").get_text(strip=True)
		bio = page_soup.find("div", "cast-bio").get_text(strip=True).replace(",", "|")

		cast.append([name, bio, num])


df = pd.DataFrame(cast)
df.to_csv('Survivor_Cast.csv', index=False)
		#f.write(name + "," + bio + "\n")
#f.close()

