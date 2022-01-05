import requests

response=requests.get("https://www.naver.com")
html=response.text
;print(html)
soup=beautifulsoup(html, 'html.parser')
word=soup.select_one("#NM_set_home_btn")
print(word.text)
