import requests
from bs4 import BeautifulSoup
import urllib

# 웹 페이지를 구해 해석한다.
load_url = "http://python.cyber.co.kr/pds/books/python2nd/test2.html"
html = requests.get(load_url)
soup = BeautifulSoup(html.content,"html.parser")

# 모든 img 태그를 검색해 링크를 구한다
for element in soup.find_all("img") :
    src = element.get("src")

    # 절대 URL과 파일을 표시한다.
    image_url = urllib.parse.urljoin(load_url, src)
    filename = image_url.split("/")[-1]
    print(image_url,">>",filename)

