import requests
import re
from bs4 import BeautifulSoup
import time

header = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36", "Accept-Language": "ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3"}
url = "https://play.google.com/store/movies?hl=ko&gl=US"
res = requests.get(url=url, headers=header,timeout=3)

res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

movies = soup.find_all("div", attrs={"class" : "VfPpkd-EScbFb-JIbuQc UVEnyf"})

print(movies[0].text)