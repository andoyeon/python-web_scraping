import requests
from bs4 import BeautifulSoup


url = 'https://search.daum.net/search?w=news&q=%EB%A8%B8%EC%8B%A0%20%EB%9F%AC%EB%8B%9D&DA=PGD&spacing=0&p=1'

# 사이트(웹 서버)에 요청(request)를 보냄
html = requests.get(url).text.strip()   # 요청의 결과(응답, response - HTML)를 저장
print(html[0:100])  # 전체 문자열에서 100자만 확인

# BeautifulSoup 객체를 생성
soup = BeautifulSoup(html, 'html5lib')

# HTML 문서의 모든 링크에 걸려 있는 주소들을 출력
links = soup.find_all('a')
for link in links:
   print(link.get('href'))


# 관심 있는 링크(뉴스 링크)들만 찾을 수 있는 방법을 고민(주말 동안)
div_coll_cont = soup.find_all(class_='coll_cont')
# soup.find_all(attrs={'class': 'coll_cont'})
print(len(div_coll_cont))   # 같은 클래스 이름이 있는 모든 HTML 요소들을 찾음
