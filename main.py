from selenium import webdriver
from decouple import config

USERNAME = config('INSTA_USER')
PASSWORD = config('INSTA_PASS')

driver = webdriver.Firefox()
start_url = "https://www.instagram.com/accounts/login/"
driver.get(start_url)
driver.implicitly_wait(5)




