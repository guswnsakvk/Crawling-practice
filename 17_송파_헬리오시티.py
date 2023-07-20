from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

url = "https://www.daum.net/"

options = Options()

options.add_argument("--start-maximized")
options.add_experimental_option("detach", True)
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36")
options.add_argument("accept-language=ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3")
driver = webdriver.Chrome(options=options)

# 다음으로 접속
driver.get(url)

# 검색바에 송파 헬리오시티 적기
driver.implicitly_wait(2)

search_bar = driver.find_element(By.CLASS_NAME, "tf_keyword")
search_bar.send_keys("송파 헬리오시티")

# 송파 헬리오시티 검색
search_btn = driver.find_element(By.CLASS_NAME, "btn_search")
search_btn.click()

# 송파 헬리오시티 정보가 있는 사이트 url 찾기
song_pa = driver.find_element(By.CLASS_NAME, "tit_place")
url = song_pa.get_attribute("href")

# 송파 헬리오시티 정보가 있는 사이트로 이동하기
driver.get(url)

# 매물보러가기
driver.implicitly_wait(5)
memul = driver.find_element(By.XPATH, "//*[@id=\"sale-count-button\"]/div/div")
memul.click()

# 매물정보가져오기
time.sleep(5)
product = driver.find_element(By.XPATH, "//*[@id=\"__next\"]/div[2]/div[2]/ul/li/a/div")
print(product)
#products = driver.find_elements(By.CLASS_NAME, "items_text_wrap__XAudD")
#print(products)