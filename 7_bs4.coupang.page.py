import requests
import re
from bs4 import BeautifulSoup

header = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36", "Accept-Language": "ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3"}

for i in range(1, 6):

  print('현재 페이지 : ' + str(i))
  url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=&backgroundColor=".format(i)
  res = requests.get(url=url, headers=header,timeout=3)

  res.raise_for_status()

  soup = BeautifulSoup(res.text, "lxml")

  #notebooks = soup.find_all("li", attrs={"class" : "search-product"})
  notebooks = soup.find_all("li", attrs={"class" : re.compile("^search-product")})

  for notebook in notebooks:
      name = notebook.find("div", attrs={"class" : "name"}).get_text()
      if 'Apple' in name:
          continue
      
      price = notebook.find("strong", attrs={"class" : "price-value"})
      if price:
          price = price.get_text()
      else:
          continue

      rating = notebook.find("em", attrs={"class" : "rating"})
      if rating:
          rating = rating.get_text()
      else:
          continue
      
      rating_cnt = notebook.find("span", attrs={"class" : "rating-total-count"})
      
      if rating_cnt:
          rating_cnt = rating_cnt.get_text()
      else:
          continue
      
      if float(rating) >= 4.5 and int(rating_cnt[1:-1]) >= 100:
        link = notebook.find("a", attrs={"class" : "search-product-link"})
        print(name)
        print(price)
        print(rating)
        print(rating_cnt)
        print('https://www.coupang.com/' + link["href"])
        print('---')