import requests
from bs4 import BeautifulSoup
import pyautogui

keyword = pyautogui.prompt("검색어 입력:")
lastpage = pyautogui.prompt("몇 페이지 까지?")
pagenum = 1
for i in range(1, int(lastpage) * 10, 10): #문자열인 lastpage를 정수형으로 변환
    print(f"====   {pagenum} 페이지  ==========================================")
    response = requests.get(f"https://search.naver.com/search.naver?where=news&sm=tab_jum&query={keyword}&start={i}")
    # 쌍따옴표 안에 중괄호, f-string
    html = response.text

    soup = BeautifulSoup(html, 'html.parser')
    links = soup.select(".news_tit")
    print(links)

    for link in links:
        title = link.text
        url = link.attrs['href']
        print(title, url)
    pagenum = pagenum+1
