import requests
from bs4 import BeautifulSoup

header = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}

# 날씨 부분
url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%B6%80%EC%82%B0+%EB%82%A0%EC%94%A8"
res = requests.get(url, headers=header)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")

temperature = soup.find("div", attrs={"class" : "temperature_text"})

summary = soup.find("p", attrs={"class" : "summary"}).getText().split(" ")

item_today = soup.find_all("li", attrs={"class" : "item_today level2"})

print("[오늘의 날씨]")
print(summary[4] + ", " + summary[0] + summary[1] + summary[2])
print("현재 " + temperature.text[6:])

for item in item_today[:3]:
    print(item.text.strip())
print()

# 뉴스 헤드라인
url = "https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=105"
res = requests.get(url, headers=header)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")

head_line = soup.find_all("a", attrs={"class" : "sh_text_headline nclicks(cls_sci.clsart)"})

print("[헤드라인 뉴스]")

for index, head in enumerate(head_line):
    print(str(index+1) + ". " + head.text)
    print("링크 : " + head["href"])
print()

# 해커스 오늘의 영어 회화
url = "https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english&keywd=haceng_submain_lnb_eng_I_others_english&logger_kw=haceng_submain_lnb_eng_I_others_english"
res = requests.get(url, headers=header)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")

conv_txt = soup.find_all("div", attrs={"class" : "conv_txt"})

print("[오늘의 회화]")

for conv in conv_txt:
    text_list = conv.text.split("\n")

    for text in text_list:
        if text != '':
            print(text)

    print()