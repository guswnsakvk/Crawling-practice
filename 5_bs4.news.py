import requests
from bs4 import BeautifulSoup

header = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}
url = "https://news.naver.com/"
res = requests.get(url, headers=header)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
# class 속성이 cjs_age_item 인 모든 "li" 태그 반환
news_agencys = soup.find_all("li", attrs={"class" : "cjs_age_item"})

#for news_agency in news_agencys:
#    print(news_agency.get_text().strip())

news = soup.find_all("div", attrs={"class" : "cjs_journal_wrap _item_contents"})
#print(news)

#link = news[0].a["href"]
#print(link)

for new in news:
    title = new.find("div", attrs={"class" : "cjs_t"})
    print(title.get_text())