from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

PATH = "/opt/anaconda3/bin/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("https://www.walmart.ca/en/lounge-co/N-1275528")

file = []
file.append(["product_name", "price", "available_online", "available_instore", "rating", "num_reviews"])

try:
	shelfThumbs = WebDriverWait(driver, 10).until(
		EC.presence_of_element_located((By.ID, "shelf-thumbs"))
	)
	articles = shelfThumbs.find_elements_by_tag_name("article")
	time.sleep(1)

	for article in articles:
		name = article.find_elements_by_class_name("thumb-header")[0].text
		rating = article.find_elements_by_class_name("ratings")[0].find_elements_by_tag_name("div")[0].get_attribute("class")
		num_reviews = article.find_elements_by_class_name("review-count")[0].text
		price = article.find_elements_by_class_name("price-current")[0].find_elements_by_tag_name("div")[0].text.replace("\n", "")
		available_online = article.find_elements_by_class_name("availability-messages")[0].find_elements_by_tag_name("div")[0].find_elements_by_tag_name("span")[0].text
		available_instore = article.find_elements_by_class_name("availability-messages")[0].find_elements_by_tag_name("div")[1].text
		
		file.append([name, price, available_online, available_instore, rating, num_reviews])




finally:
	driver.quit()
	df = pd.DataFrame(file)
	df.to_csv("Walmart_Lounge_and_Co.csv", index=False)