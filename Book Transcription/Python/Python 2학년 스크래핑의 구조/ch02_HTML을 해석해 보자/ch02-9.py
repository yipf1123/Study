import requests
from bs4 import BeautifulSoup
import urllib

# 웹 페이지를 구해 해석한다
load_url = "http://python.cyber.co.kr/pds/books/python2nd/test2.html"
html = requests.get(load_url)
soup = BeautifulSoup(html.content,"html.parser")

# 모든 a태그그를 검색하고 링크를 절대 URL로 표시한다.
for element in soup.find_all("a"):
    print(element.text)
    url = element.get("href")
    link_url = urllib.parse.urljoin(load_url, url)
    print(link_url)