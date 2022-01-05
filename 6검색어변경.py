import requests
from bs4 import BeautifulSoup

keyword = input("검색어 입력:")
response = requests.get("https://search.naver.com/search.naver?where=news&sm=tab_jum&query=" + keyword)
html = response.text

soup = BeautifulSoup(html, 'html.parser')
links = soup.select(".news_tit")
print(links)

for link in links:
    title = link.text
    url = link.attrs['href']
    print(title, url)

