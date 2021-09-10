from selenium import webdriver
from decouple import config

USERNAME = config('INSTA_USER')
PASSWORD = config('INSTA_PASS')

driver = webdriver.Firefox()
start_url = "https://www.instagram.com/accounts/login/"
driver.get(start_url)
driver.implicitly_wait(5)

username_input = driver.find_element_by_name('username')
password_input = driver.find_element_by_name('password')
login_button = driver.find_element_by_tag_name('button')
username_input.send_keys(USERNAME)
password_input.send_keys(PASSWORD)
login_button.click()


if driver.find_element_by_xpath('//button[text()="Not Now"]'):
    driver.find_element_by_xpath('//button[text()="Not Now"]').click() # notification_button 

driver.save_screenshot("screenshot.png")
driver.close()

