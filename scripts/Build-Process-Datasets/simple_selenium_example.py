from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:39.0) Gecko/20100101 Firefox/39.0')


driver = webdriver.Chrome(options = options)
driver.set_page_load_timeout(30)

# Take action on browser
driver.get("http://www.python.org")

# Request browser information
title = driver.title

#Establish Waiting Strategy
driver.implicitly_wait(0.5)

#Find an element
elem = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[1]/div/ul/li[1]/a')
print(elem.text)

#end driver session
driver.quit()
