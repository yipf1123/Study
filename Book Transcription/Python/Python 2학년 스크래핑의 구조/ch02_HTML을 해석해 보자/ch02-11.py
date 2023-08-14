import requests

# 이미지 파일을 구한다.
image_url = "http://python.cyber.co.kr/pds/books/python2nd/sample1.png"
imgdata = requests.get(image_url)

# URL에서 마지막에 있는 파일명을 추출한다.
filename = image_url.split("/")[-1]

# 이미지 데이터를 파일에 쓴다.
with open(filename, mode="wb") as f:
 f.write(imgdata.content)
