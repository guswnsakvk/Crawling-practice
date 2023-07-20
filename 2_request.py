import requests

res = requests.get("https://google.com")
#res = requests.get("https://nadocoding.tistory.com")
res.raise_for_status()
print(res.status_code)

#if res.status_code == requests.codes.ok:
#    print("정상입니다")
#else:
#    print("문제가 생겼습니다.")

print("웹 스크래핑을 진행합니다")
print((len(res.text)))
print(res.text)

with open("mygoole.html", "w", encoding="utf8") as f:
    f.write(res.text)