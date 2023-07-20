import requests
from bs4 import BeautifulSoup

header = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}
url = "https://realty.daum.net/home/apt/danjis/38487/items?_url=%2Frealty%2Fapt%2Fdanjis%2F38487%2Fitems&danjiId=38487&requestId=38487&canUseDirectConsulting=false&danjiZedStatus=%EB%AF%B8%EC%A7%80%EC%9B%90&app_version=&mkt_source=&messagingJob=%EC%A0%9C%ED%9C%B4%EB%8B%A8%EC%A7%80%EB%AC%B8%EC%9D%98&adid=&uuid=&phone=&userNo=&appVersion=&platform=www&make=&model=&modelVersion=&platformVersion=&deviceIP=&timezone=&zid=005ad070-1fb4-11ee-a087-b5a25d2b28b2&business_type=%EB%B6%80%EB%8F%99%EC%82%B0"
res = requests.get(url, headers=header)
res.raise_for_status()
soup = BeautifulSoup(res.text)

with open("quiz.html", "w", encoding="utf8") as f:
    f.write(soup.prettify())