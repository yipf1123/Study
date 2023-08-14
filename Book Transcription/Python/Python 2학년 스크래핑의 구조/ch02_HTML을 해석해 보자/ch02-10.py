import requests
from bs4 import BeautifulSoup
import urllib

# 웹 페이지를 구해 해석한다.
load_url ="http://python.cyber.co.kr/pds/books/python2nd/test2.html"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")

# 파일을 쓰기 모드로 연다.
filename = "linklist.text"
with open(filename, "w") as f:
    # 모든 a 태그를 검색하고 링크를 절대 URL로 보낸다.
    for element in soup.find_all("a"):
        url = element.get("href")
        link_url =urllib.parse.urljoin(load_url, url)
        f.write(element.text+"\n")
        f.write(link_url+"\n")
        f.write("\n")


