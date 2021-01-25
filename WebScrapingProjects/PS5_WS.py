from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import tkinter as tk
import time




EMAIL = "bjbl"
FNAME = "bljb"
LNAME = "bjb"
ADDRESS = "jblj"
CITY = "ljnj"
PROVINCE = "iolhkj"
POSTAL = "87087"
PHONE = "9686986"
CARDNUMBER = "3333333333333333"
EMONTH = "09"
EYEAR = "99"
SCODE = "999"
PATH = "ljbkjbk"
Test="https://www.walmart.ca/en/ip/PS5-Game-Console-Handle-Protector-Silicone-Handle-and-Push-Button-Cover-8-in-1-set-Protective-Joystick-Caps/26691DW5XY5B"
Real="https://www.walmart.ca/en/ip/playstation5-console/6000202198562"
DELAY = 0

window = tk.Tk()

tk.Label(text="Email").pack()
email = tk.Entry()
email.pack()




tk.Label(text="First Name").pack()
fname = tk.Entry()
fname.pack()

FNAME = fname.get()
EMAIL = email.get()


window.mainloop()

print(EMAIL)
print(FNAME)



driver = webdriver.Chrome(PATH)
driver.get(Test)

try:
	add_to_cart_button = WebDriverWait(driver, 1200).until(
		EC.presence_of_element_located((By.XPATH, ".//*[contains(text(),'Add to cart')]"))
	)
	driver.find_elements(By.XPATH, ".//*[contains(text(),'Close')]")[0].click()
	ActionChains(driver).move_to_element(add_to_cart_button).click().perform()
	time.sleep(DELAY)
	WebDriverWait(driver, 120).until(
		EC.presence_of_element_located((By.XPATH, ".//*[contains(text(),'Checkout')]"))
	).click()
	time.sleep(DELAY)
	WebDriverWait(driver, 120).until(
		EC.presence_of_element_located((By.XPATH, ".//*[contains(text(),'Proceed to checkout')]"))
	).click()
	time.sleep(DELAY)
	WebDriverWait(driver, 120).until(
		EC.presence_of_element_located((By.XPATH, "//*[@id='email']"))
	).send_keys(EMAIL)
	time.sleep(DELAY)
	WebDriverWait(driver, 120).until(
		EC.presence_of_element_located((By.XPATH, "//*[@id='step1']/div[2]/form/div/div[5]/button"))
	).click()


	time.sleep(DELAY)
	WebDriverWait(driver, 120).until(
		EC.presence_of_element_located((By.XPATH, "//*[@id='shipping-tab']"))
	).click()
	time.sleep(DELAY)
	WebDriverWait(driver, 120).until(
		EC.presence_of_element_located((By.XPATH, "//*[@id='firstName']"))
	).send_keys(FNAME)
	time.sleep(DELAY)
	WebDriverWait(driver, 120).until(
		EC.presence_of_element_located((By.XPATH, "//*[@id='lastName']"))
	).send_keys(LNAME)
	time.sleep(DELAY)
	WebDriverWait(driver, 120).until(
		EC.presence_of_element_located((By.XPATH, "//*[@id='address1']"))
	).send_keys(ADDRESS)
	time.sleep(DELAY)
	WebDriverWait(driver, 120).until(
		EC.presence_of_element_located((By.XPATH, "//*[@id='city']"))
	).send_keys(CITY)
	time.sleep(DELAY)
	WebDriverWait(driver, 120).until(
		EC.presence_of_element_located((By.XPATH, "//select[@id='province']/option[text()='Ontario']"))
	).click()
	time.sleep(DELAY)
	WebDriverWait(driver, 120).until(
		EC.presence_of_element_located((By.XPATH, "//*[@id='postalCode']"))
	).send_keys(POSTAL)
	time.sleep(DELAY)
	WebDriverWait(driver, 120).until(
		EC.presence_of_element_located((By.XPATH, "//*[@id='phoneNumber']"))
	).send_keys(PHONE)
	time.sleep(DELAY)
	driver.execute_script("document.body.style.transform='scale(0.3)';")
	time.sleep(DELAY+1)
	
	WebDriverWait(driver, 120).until(
		EC.visibility_of_element_located((By.XPATH, "//*[contains(text(),'Next')]"))
	).click()
	time.sleep(DELAY)

	WebDriverWait(driver, 120).until(
		EC.visibility_of_element_located((By.XPATH, "//*[contains(text(),'Next')]"))
	).click()
	time.sleep(DELAY)

	next_button3 = WebDriverWait(driver, 120).until(
		EC.visibility_of_element_located((By.XPATH, "//*[@id='step2']/div[2]/div[2]/div/div/div[2]/div[2]/div/div[2]/button"))
	)
	ActionChains(driver).move_to_element(next_button3).click().perform()
	time.sleep(DELAY)

	WebDriverWait(driver, 120).until(
		EC.presence_of_element_located((By.XPATH, "//*[@id='cardNumber']"))
	).send_keys(CARDNUMBER)
	time.sleep(DELAY)
	WebDriverWait(driver, 120).until(
		EC.presence_of_element_located((By.XPATH, "//*[@id='expiryMonth']"))
	).send_keys(EMONTH)
	time.sleep(DELAY)
	WebDriverWait(driver, 120).until(
		EC.presence_of_element_located((By.XPATH, "//*[@id='expiryYear']"))
	).send_keys(EYEAR)
	time.sleep(DELAY)
	WebDriverWait(driver, 120).until(
		EC.presence_of_element_located((By.XPATH, "//*[@id='securityCode']"))
	).send_keys(SCODE)
	time.sleep(DELAY)

	WebDriverWait(driver, 120).until(
		EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'Apply')]"))
	).click()
	time.sleep(100)

	print("done")
finally:
	driver.quit()