#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 11:51:36 2020

@author: isaacmuscat
"""
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.newegg.ca/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20cards'

# opening up connection, grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# html parser
page_soup = soup(page_html, "html.parser")

#grabs each product
containers = page_soup.findAll("div",{"class":"item-container"})

filename = "products.csv"
f = open(filename, "w")
headers = "brand, product_name, shipping\n"
f.write(headers)


for container in containers:
	brand = container.findAll('a', {'class':'item-brand'})[0].img["title"]
	product_name  = container.findAll('a', {'class':'item-title'})[0].text
	shipping = container.findAll("li", {"class":"price-ship"})[0].text.strip()


	print("brand" + brand)
	print("product_name" + product_name)
	print("shipping" + shipping)

	f.write(brand + "," + product_name.replace(",", "|") + "," + shipping + "\n")

f.close()
