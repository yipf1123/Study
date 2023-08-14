import requests
from pathlib import Path

# 저장용 폴더를 만든다.
out_folder = Path("download")
out_folder.mkdir(exist_ok=True)

# 이미지 파일을 구한다.
image_url = "http://python.cyber.co.kr/pds/books/python2nd/sample1.png"
imgdata = requests.get(image_url)

# URL에서 마지막에 있는 파일명을 추출하고 저장 폴더명과 연결한다.
filename = image_url.split("/")[-1]
out_path = out_folder.joinpath(filename)

# 이미지 데이터 파일을 쓴다
with open(out_path, mode="wb") as f:
    f.write(imgdata.content)