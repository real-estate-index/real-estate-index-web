import re
import random
import requests
from bs4 import BeautifulSoup as bs
from .models import News, Issue


def clean_html(x): # title, description에 있는 찌꺼기 제거
  x = re.sub("\&\w*\;","",x)
  x = re.sub("<.*?>","",x)
  if len(x) > 40: # 40글자가 넘으면 요약
      x = x[:40]+'...'
  return x

def news_api():
    search_word = "한국 부동산" # 네이버 뉴스 검색 키워드
    display = 10 # API에서 가져올 뉴스 기사 수
    sort = "sim"
    client_id = "{}" # 네이버 API 사용자 ID
    client_key = "{}" # 네이버 뉴스 API 키
    url = f"https://openapi.naver.com/v1/search/news?query={search_word}&display={display}&sort={sort}" # 네이버 뉴스 API 주소
    headers = {"X-Naver-Client-Id":client_id,"X-Naver-Client-Secret":client_key} # 헤더 설정
    req = requests.get(url,headers=headers) # requests로 API 호출
    if req.status_code == 200: # API가 정상 호출
        News.objects.all().delete() # 기존 데이터베이스(News 테이블) 초기화
        news = req.json()["items"] # json형태로 API 호출 후 items에 있는 정보만 저장
        for item in news: # news의 딕셔너리 하나씩 확인
            title = clean_html(item["title"]) # title key의 value 저장
            description = clean_html(item["description"]) # description key의 value 저장
            link = item["link"] # link key의 value 저장
            News.objects.create(title=title, description=description, link=link) #데이터베이스에 저장
    else: #API 비정상 호출
        print(f"Error Code: {req.status_code}") #에러코드 출력

def issues_crawling(): #이슈 크롤링
    num = [2,9]
    Issue.objects.all().delete()
    for i in range(2):
        url = f"https://www.molit.go.kr/USR/NEWS/m_71/lst.jsp?search_section=p_sec_{num[i]}"
        page = requests.get(url)
        soup = bs(page.text, "html.parser")
        for i,item in enumerate(soup.select("td.bd_title>a")):
            if i == 5:
                break
            title = item.text.strip()
            link = url[0:38] + item.attrs['href']
            Issue.objects.create(title=title, link=link)

def calculate():
    val = random.randint(0,100)
    return val
