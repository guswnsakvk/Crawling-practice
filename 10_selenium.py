from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

url = "https://naver.com"

options = Options()

options.add_argument("--start-maximized")
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get(url)

time.sleep(2)

#driver.find_element(By.CLASS_NAME, "search_input").send_keys("우주")
#time.sleep(2)

#driver.find_element(By.ID, "query").send_keys("햄버거")

#login_btn = driver.find_element(By.CLASS_NAME, "MyView-module__link_login___HpHMW")
#print(login_btn)
#login_btn.click()

#elem =  driver.find_element(By.CLASS_NAME, "search_input")
#elem.send_keys("나도코딩")
#elem.send_keys(Keys.ENTER)

elem = driver.find_elements(By.TAG_NAME, 'a')
print(elem)
for e in elem:
    print(e.get_attribute("href"))