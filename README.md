# 크롤링 정리
크롤링은 웹 페이지에 있는 데이터를 추출해 내는 것을 말합니다.

## 크롤링하는 방법
### 1\. python + Beautiful Soup  
- 크롤링할 때 많이 사용하는 방법

### 2\. python + selenium  
- 동적 웹 페이지나 JavaScript가 로드되는 페이지의 데이터를 가져올 수 있는 방법

## Beautiful Soup
### 1. 라이브러리 설치
```python
pip install requests
pip install beautifulsoup4
pip install lxml
```

### 2. 기본 틀
```python
import requests
from bs4 import BeautifulSoup

# header를 설정하는 이유
# 사이트에 컴퓨터가 크롤링을 하려고 접속하면
# 사이트 입장에서 부화가 걸릴 수 있고 정보를 뺏길 수 있기 때문에
# 접속을 차단할 수 있음
# 이를 User-Agent로 해결할 수 있음
header = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36", "Accept-Language": "ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3"}

# 크롤링할 사이트 url
url = "https://news.naver.com/"

# 크롤링할 사이트 html 가져오기
res = requests.get(url, headers=header) 

# 크롤링할 사이트에서 값을 가져오면 계속 진행
# 값을 가져오지 못하면 프로그램 종료
res.raise_for_status()

# BeautifulSoup을 사용해서 lxml로 표현하기
soup = BeautifulSoup(res.text, "lxml")
```

### 3. 원하는 정보를 가진 태그 찾는 방법
1\. find
```python
변수이름 = soup.find(찾는 자료가 있는 태그, attrs={html 속성 이름(class, id 등등): html 속성 값(class 이름, id 이름 등등)})

ex) Nservice_subitem라는 class를 가진 span 태그를 찾아줘
sub_item1 = soup.find("span", attrs={"class" : "Nservice_subitem"})
```

2\. find_all
```python
변수이름 = soup.find_all(찾는 자료가 있는 태그, attrs={html 속성 이름(class, id 등등): html 속성 값(class 이름, id 이름 등등)})

ex) cjs_journal_wrap, _item_contents 클래스를 가진 모든 div 태그를 찾아줘
news = soup.find_all("div", attrs={"class" : "cjs_journal_wrap _item_contents"})
```

### 4. 태그에서 원하는 정보 추출하는 방법
1\. 태그에 있는 텍스트 가져오는 방법
```python
저장할 변수 이름 = 변수이름.get_text()

ex) price.get_text()
```

2\. html 속성 값 가져오는 방법
```
저장할 변수 이름 = 변수이름["가져오고 싶은 속성 이름"]

ex) head["href"], image["src"]
```

## selenium
### 1. 라이브러리 설치
```python
pip install requests
pip install selenium
pip install lxml
```

### 2. 기본 툴
```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# 크롤링할 사이트 주소
url = "https://flight.naver.com/"

# 크롤링할 때 옵션 추가
options = Options()

options.add_argument("--start-maximized")
# 크롤링하고 사이트가 안 꺼지도록 설정
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

# 크롤링할 사이트로 이동
driver.get(url)
```

### 3. 검색창에 글자 쓰기
```python
저장할 변수 이름 = 변수이름.send_keys(검색할 이름)

ex) 검색창에 제주도 입력하기
place_input.send_keys("제주도")
```

### 4. 버튼 클릭하기
```python
변수이름.click()

ex) 비행기 표 조회 버튼 클릭하기
find_flight_btn.click()
```

### 5. 원하는 값이 있는 태그 찾기
```python
저장할 변수 이름 = driver.find_element(By.(CLASS_NAME|ID|TAG_NAME 등등), By뒤에 있는 거에 맞는 값)

ex) MyView-module__link_login___HpHMW 클래스를 가진 요소를 찾아줘
lem = driver.find_element(By.CLASS_NAME, "MyView-module__link_login___HpHMW")
```