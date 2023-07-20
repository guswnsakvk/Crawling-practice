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

# 1. 네이버 이동
driver.get(url)

time.sleep(2)

# 2. 로그인 버튼 클릭
elem = driver.find_element(By.CLASS_NAME, "MyView-module__link_login___HpHMW")
elem.click()

time.sleep(2)

# 3. id, pw 입력
login_id = driver.find_element(By.ID, "id")
login_pw = driver.find_element(By.ID, "pw")

login_id.send_keys("123")
login_pw.send_keys("123")

# 4. 로그인 버튼 클릭
login_btn = driver.find_element(By.ID, "log.login")
login_btn.click()

time.sleep(1)

# 5. id, pw 지우기
#login_id.clear()
#login_pw.clear()

# 6. html 정보 출력
print(driver.page_source)

# 7. 브라우저 종료
# driver.quit() 전체 브라우저 종료
driver.close() # 현재 탭만 종료