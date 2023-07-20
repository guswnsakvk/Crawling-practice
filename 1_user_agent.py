import requests

url = "http://nadocoding.tistory.com"
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}
res = requests.get(url, headers)
res.raise_for_status()
with open("mygoole.html", "w", encoding="utf8") as f:
    f.write(res.text)