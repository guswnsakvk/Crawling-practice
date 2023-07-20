import requests
import re
from bs4 import BeautifulSoup

header = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36", "Accept-Language": "ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3"}
url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=&backgroundColor="
res = requests.get(url=url, headers=header,timeout=3)

res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

#notebooks = soup.find_all("li", attrs={"class" : "search-product"})
notebooks = soup.find_all("li", attrs={"class" : re.compile("^search-product")})
#print(notebooks)

for notebook in notebooks:
    name = notebook.find("div", attrs={"class" : "name"}).get_text()
    price = notebook.find("strong", attrs={"class" : "price-value"})
    if price:
        price = price.get_text()
    else:
        price = '가격 없음'

    rating = notebook.find("em", attrs={"class" : "rating"})
    if rating:
        rating = rating.get_text()
    else:
        rating = "평점 없음"
    
    rating_cnt = notebook.find("span", attrs={"class" : "rating-total-count"})
    
    if rating_cnt:
        rating_cnt = rating_cnt.get_text()
    else:
        rating_cnt = "평점없음"

    print(name)
    print(price)
    print(rating)
    print(rating_cnt)
    print('---')