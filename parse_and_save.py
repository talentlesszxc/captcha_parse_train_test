from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.firefox.options import Options
import wget
import time

options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)

count = 200
for i in range(count):
    driver.get("https://freebitco.in")
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    value = soup.find('input', {'class':'captchasnet_captcha_random'})['value']
    site = 'https://captchas.freebitco.in/botdetect/e/live/images/' + value + '.jpeg'
    #print(site)
    wget.download(site, 'new_captchas/')
    time.sleep(2)    
    print("\nDownloaded " + str(i+1) + " of " + str(count) + " images")

print ("DONE!")

driver.quit()