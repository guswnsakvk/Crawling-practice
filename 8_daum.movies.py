import requests
import re
from bs4 import BeautifulSoup

header = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36", "Accept-Language": "ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3"}
url = "https://search.daum.net/search?w=tot&q=2022%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR"
res = requests.get(url=url, headers=header,timeout=3)

res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
#print(res.text)

for year in range(2019, 2023):
    url = "https://search.daum.net/search?w=tot&q={}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR".format(year)
    res = requests.get(url=url, headers=header, timeout=3)

    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    
    images = soup.find_all("img", attrs={"class" : "thumb_img"})
    for index, image in enumerate(images):
      image_url = image["src"]

      image_res = requests.get(image_url)
      image_res.raise_for_status()

      with open("year{}movie{}.jpg".format(year,index+1), "wb") as f:
        f.write(image_res.content)