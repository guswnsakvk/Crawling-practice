import requests
from bs4 import BeautifulSoup

header = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}
url = "https://news.naver.com/"
res = requests.get(url, headers=header)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
#print(soup.title)
#print(soup)
#print(soup.title.get_text())
#print(soup.header)
#print(soup.find("div", attrs={"class" : "Ngnb_service"}))

sub_item1 = soup.find("span", attrs={"class" : "Nservice_subitem"})
#print(sub_item1.next_sibling.next_sibling)
#print(sub_item1.span.get_text())
#print(sub_item1.parent)
#print(sub_item1.find_next_sibling("span"))

print(sub_item1.find_next_siblings("span"))