"""
다음 '머신러닝' 뉴스 100개의 기사 제목, 주소, 내용을 출력하는 함수
"""
import requests
from bs4 import BeautifulSoup


def daum_search(keyword):
    url = 'https://search.daum.net/search?w=news&nil_search=btn&DA=NTB&enc=utf8&cluster=y&'

    # 1~10 페이지
    for page in range(1, 2):
        print('===Page{}==='.format(page))
        req_params = {
            'p': page,
            'q': keyword
        }
        # 요청보내기
        response = requests.get(url, params=req_params)
        html = response.text.strip()

        soup = BeautifulSoup(html, 'html5lib')

        news_links = soup.select('a.f_link_b')
        for link in news_links:
            news_url = link.get('href')
            news_title = link.text
            print(news_title)
            print(news_url)
            news_contents(news_url)




def news_contents(url):
    response = requests.get(url)
    # html = response.text.strip()
    html = response.content

    soup = BeautifulSoup(html.decode('utf-8', 'replace'), 'html5lib')

    # contents = soup.find('div', class_='par').p.text
    contents = soup.select('div.par')
    for i in range(len(contents)):
        print(contents[i].text.strip())




if __name__ == '__main__':
    daum_search(keyword='머신러닝')

    # url = 'https://biz.chosun.com/site/data/html_dir/2020/08/31/2020083101015.html'
    # news_contents(url)