### beautifulsoup4. webscraping module 사용
from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())

# pip 명령어
# pip list : 현재 설치된 패키지 목록 나열
# pip show 패키지명 : 패키지명에 대한 정보 출력
# pip install --upgrade 패키지명 : 패키지 버전 업그레이드
# pip uninstall 패키지명 : 패키지 삭제