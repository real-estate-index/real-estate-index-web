import re
import os
import requests
import pandas as pd
import datetime as dt
from django.conf import settings
from bs4 import BeautifulSoup as bs
from .models import News, Issue, Region, District, DistrictIndex, SentimentIndex, TradePrice, TradeAmount, Momentum


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

def open_files():
    file_path = os.path.join(settings.BASE_DIR,'real_estate_app', 'data', 'index_source', 'seoul')
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"지정된 경로를 찾을 수 없습니다: {file_path}")
    files_in_directory = os.listdir(file_path)
    data_set = []
    for i,file in enumerate(files_in_directory):
        with open(file_path + "/" + file, encoding='utf-8') as data_file:
            lines = data_file.readlines()
            globals()["".format(file[:2])] = [file[:2],i+1]
            date, cases, prices = [], [], []
            for line in lines[-28:]:
                d,c,p = line.strip().split(",")
                date.append(d)
                cases.append(c)
                prices.append(p)
            globals()["".format(file[:2])].append(date)
            globals()["".format(file[:2])].append(cases)
            globals()["".format(file[:2])].append(prices)
            data_set.append(globals()["".format(file[:2])])
    file_path = os.path.join(settings.BASE_DIR, 'real_estate_app', 'data', 'update_data_function', 'others')
    with open(file_path + "/네이버트렌드_부동산검색.csv",encoding = "utf-8") as file:
        lines = file.readlines()
    now = dt.datetime.now()
    now = now.date()
    now = str(now).replace("-","")[:6]
    now = now.replace("06","02")
    calc = []
    for line in lines:
        try:
            date, trend = line.strip().split(",")
            date = date.replace("-","")[:6]
            if date == now:
                calc.append(float(trend))
        except:
            pass
    len_calc = len(calc)
    calc = sum(calc)/len_calc
    file_path = os.path.join(settings.BASE_DIR, 'real_estate_app', 'data', 'mind')
    with open(file_path+"/mind_standard_data.csv",encoding = "utf-8") as file:
        lines = file.readlines()
    mind = []
    for line in lines:
        data = line.strip().split(",")
        if data[2] == "서울특별시":
            mind.append([data[1].replace("-","")[:6],float(data[5])])
    return data_set, calc, mind


def open_incheon():
    file_path = os.path.join(settings.BASE_DIR, 'real_estate_app', 'data', 'index_source', 'incheon')
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"지정된 경로를 찾을 수 없습니다: {file_path}")
    files_in_directory = os.listdir(file_path)
    for i,file in enumerate(files_in_directory):
        data_set = []
        with open(file_path + "/" + file, encoding = "utf-8") as data_file:
            lines = data_file.readlines()
            for line in lines[-15:]:
                try:
                    line = line.strip().split(",")
                    data_set.append([line[0],float(line[3]),float(line[4]),float(line[5]),float(line[7])])
                except:
                    pass
        calculate_data_incheon(i+26, line[-1], data_set)

def read_data():
    data_set, trending, mind = open_files()
    for data in data_set:
        expanded_data = []
        for i in range(len(data[3])):
            expanded_data.append([data[0],data[1],data[2][i],data[3][i],float(data[4][i])])
        df = pd.DataFrame(expanded_data,columns = ["region","id","date","cases","prices"])
        calculate_data_seoul(df,trending, mind)
    open_incheon()

def calculate_data_incheon(i, index, data_set):
    df = pd.DataFrame(data_set, columns = ["date","amount", "momentum", "price", "mind"])
    id = i
    fg_idx = float(index)
    date = list(df["date"])
    price = list(df["price"])
    s_idx = list(df["mind"])
    scaled_volume_diff = list(df["amount"])
    scaled_momentum_2m = list(df["momentum"])
    save_fg_idx(id, standardize_values(fg_idx))
    save_s_idx(date, s_idx, id)
    save_price(date, price, id)
    save_amount(date, scaled_volume_diff, id)
    save_momentum(date, scaled_momentum_2m, id)
def calculate_data_seoul(df,trending, mind):
    df["price_change"] = df["prices"].pct_change() * 100
    df['volatility_3m'] = df['price_change'].rolling(window=3).std()
    df['volatility_12m'] = df['price_change'].rolling(window=12).std()
    df['volume_3m'] = df['cases'].rolling(window=3).mean()
    df['volume_12m'] = df['cases'].rolling(window=12).mean()
    df['momentum_2m'] = df['price_change'].rolling(window=2).mean() * df['cases'].rolling(window=2).mean()
    df['volatility_diff'] = df['volatility_3m'] - df['volatility_12m']
    df['volume_diff'] = df['volume_3m'] - df['volume_12m']
    min_max_values = {
        'volatility_diff': (df['volatility_diff'][-12:].min(), df['volatility_diff'][-12:].max()),
        'volume_diff': (df['volume_diff'][-12:].min(), df['volume_diff'][-12:].max()),
        'momentum_2m': (df['momentum_2m'][-12:].min(), df['momentum_2m'][-12:].max())
    }
    scaled_volatility_diff = scaling(df["volatility_diff"][-12:].mean(), * min_max_values["volatility_diff"])
    scaled_volume_diff = scaling(df["volume_diff"][-12:].mean(), * min_max_values["volume_diff"])
    scaled_momentum_2m = scaling(df["momentum_2m"][-12:].mean(), *min_max_values["momentum_2m"])


    weights = {
        'scaled_volatility_diff': 0.125,
        'scaled_volume_diff': 0.125,
        'scaled_momentum_2m': 0.35,
        'search_mean': 0.15,
        'normalized_DT': 0.25
    }
    fear_greed_idx = (weights["scaled_volatility_diff"] * scaled_volatility_diff
                      + weights["scaled_volume_diff"] * scaled_volume_diff
                      + weights["scaled_momentum_2m"] * scaled_momentum_2m
                      + weights["search_mean"] * trending
                      + weights["normalized_DT"] * mind[-1][-1])
    scaled_volume_diff = []
    scaled_momentum_2m = []
    for i in range(13,len(df)):
        min_max_values = {'volume_diff': (df['volume_diff'][i-13:i].min(), df['volume_diff'][i-13:i].max()),
        'momentum_2m': (df['momentum_2m'][i-13:i].min(), df['momentum_2m'][i-13:i].max())}
        scaled_volume_diff.append(scaling(df["volume_diff"][i-13:i].mean(), *min_max_values["volume_diff"]))
        scaled_momentum_2m.append(scaling(df["momentum_2m"][i-13:i].mean(), *min_max_values["momentum_2m"]))
    df = df[-15:]
    date = list(df["date"])
    id = list(df["id"])[0]
    price = list(df["prices"])
    fg_idx = fear_greed_idx
    s_idx = []
    for m in mind:
        s_idx.append(m[-1])
    s_idx = s_idx[-15:]
    save_fg_idx(id, standardize_values(fg_idx))
    save_s_idx(date, s_idx, id)
    save_price(date,price,id)
    save_amount(date,scaled_volume_diff,id)
    save_momentum(date,scaled_momentum_2m,id)

def scaling(value, min_value, max_value):
    if max_value - min_value == 0:
        return 50  # 변화가 없으면 중간값 50을 반환
    return (value - min_value) / (max_value - min_value) * 100

def standardize_values(old_value, old_min=20, old_max=70, new_min=0, new_max=100):
    if old_value > 70:
        old_value = 70
    elif old_value < 20 :
        old_value = 20
    new_value = ((old_value - old_min) * (new_max - new_min)) / (old_max - old_min) + new_min
    return int(new_value)
def save_fg_idx(id, fg_idx):
    try:
        district = District.objects.get(id=id)
        DistrictIndex.objects.create(district=district, index_value=fg_idx)
    except District.DoesNotExist:
        print(f"District with id {id} does not exist.")

def save_s_idx(dates, s_idxs, id):
    for date,s_idx in zip(dates,s_idxs):
        district = District.objects.get(id=id)
        SentimentIndex.objects.create(year_month = date, index_value = s_idx, district = district)

def save_price(dates,prices,id):
    for date,price in zip(dates,prices):
        district = District.objects.get(id=id)
        TradePrice.objects.create(year_month = date, price = price, district = district)
def save_amount(dates,cases,id):
    for date,amount in zip(dates,cases):
        district = District.objects.get(id=id)
        TradeAmount.objects.create(year_month = date, amount = amount, district = district)

def save_momentum(dates,momentums,id):
    for date,momentum in zip(dates,momentums):
        district = District.objects.get(id=id)
        Momentum.objects.create(year_month = date, momentum = momentum, district = district)
def initializing():
    regions = ["서울","인천"]
    for r in regions:
        Region.objects.create(name=r)
    file_path = os.path.join(settings.BASE_DIR, 'real_estate_app', 'data', 'index_source', 'seoul')
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"지정된 경로를 찾을 수 없습니다: {file_path}")
    files_in_directory = os.listdir(file_path)
    districts = []
    for file in files_in_directory:
        file = str(file).replace("_data_summary간단.csv","")
        if file[-1] != "구":
            file += "구"
        districts.append(file)
    for d in districts:
        name = d
        region = Region.objects.get(id = 1)
        District.objects.create(name = name, region = region)
    file_path = os.path.join(settings.BASE_DIR, 'real_estate_app', 'data', 'index_source', 'incheon')
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"지정된 경로를 찾을 수 없습니다: {file_path}")
    files_in_directory = os.listdir(file_path)
    districts = []
    for file in files_in_directory:
        file = str(file).replace("_fear_greed_index_full.csv","")
        if file[-1] != "구":
            file += "구"
        districts.append(file)
    for d in districts:
        name = d
        region = Region.objects.get(id = 2)
        District.objects.create(name = name, region = region)