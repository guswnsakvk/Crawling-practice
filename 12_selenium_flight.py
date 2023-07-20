from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import csv

url = "https://flight.naver.com/"

options = Options()

options.add_argument("--start-maximized")
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

# 1. 네이버 항공 사아트로 이동
driver.get(url)

driver.implicitly_wait(2)
# 2. 도착할 장소 선택
place = driver.find_element(By.CLASS_NAME, "end")
place.click()

place_input = driver.find_element(By.CSS_SELECTOR, "[placeholder='국가, 도시, 공항명 검색']")
place_input.send_keys("제주도")

driver.implicitly_wait(2)
place_click = driver.find_element(By.CLASS_NAME, "autocomplete_search_item__2WRSw")
place_click.click()

# 가는 날 선택
select_bar = driver.find_element(By.CLASS_NAME, "tabContent_options__KwvIB")
select_btn = select_bar.find_elements(By.TAG_NAME, "button")

#print(select_btn)

start_day = select_btn[0]
start_day.click()

find_month = driver.find_elements(By.CLASS_NAME, "month")
#print(find_month)

driver.implicitly_wait(3)
find_day = find_month[0].find_elements(By.CLASS_NAME, 'num')
find_day[11].click()

# 오는 날 선택
end_day = select_btn[1]
end_day.click()

#print(find_day[13])

driver.implicitly_wait(3)
find_month = driver.find_elements(By.CLASS_NAME, "month")
find_day = find_month[0].find_elements(By.CLASS_NAME, 'num')
find_day[13].click()

# 항공권 선택
find_flight_btn = driver.find_element(By.CLASS_NAME, 'searchBox_search__2KFn3')
find_flight_btn.click()

driver.implicitly_wait(10)

# csv 파일 세팅
filename = "항공권 정보.csv"
f = open(filename, "w", encoding="utf8", newline="")
writer = csv.writer(f)

elem = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "result")))

for e in elem:
    data = e.text.split('\n')
    writer.writerow(data)

#elem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "result")))
#elem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div/div[1]/div[6]/div/div[2]/div[2]/div/button")))
#print(elem)
#print(elem.get_attribute("outerHTML"))
#elem = driver.find_element(By.XPATH, )
