import os
import pandas as pd
import datetime as dt
from .models import DistrictIndex

def open_files():
    file_path = 'data/index_source/seoul'
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
    with open("data/update_data_function/others/네이버트렌드_부동산검색.csv",encoding = "utf-8") as file:
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
    with open("data/mind/mind_standard_data.csv",encoding = "utf-8") as file:
        lines = file.readlines()
    mind = []
    for line in lines:
        data = line.strip().split(",")
        if data[2] == "서울특별시":
            mind.append([data[1].replace("-","")[:6],float(data[5])])
    return data_set, calc, mind


def read_data():
    data_set, trending, mind = open_files()
    for data in data_set:
        expanded_data = []
        for i in range(len(data[3])):
            expanded_data.append([data[0],data[1],data[2][i],data[3][i],float(data[4][i])])
        df = pd.DataFrame(expanded_data,columns = ["region","id","date","cases","prices"])
        df = calculate_data(df,trending, mind)
        print(df)

def calculate_data(df,trending, mind):
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
    df = df[-15:]
    date = list(df["date"])
    district_id = list(df["id"])
    cases = list(df["cases"])
    price = list(df["prices"])
    fg_idx = [fear_greed_idx] * 15
    s_idx = []
    momentum = list(df["momentum_2m"])
    for m in mind:
        s_idx.append(m[-1])
    s_idx = s_idx[-15:]
    new_expanded_list = []
    for i in range(15):
        new_expanded_list.append([date[i],district_id[i],cases[i],price[i],fg_idx[i],s_idx[i],momentum[i]])
    new_df = pd.DataFrame(new_expanded_list,columns=["date",'id','cases','price','fg_idx','s_idx','momentum'])
    return new_df

def scaling(value, min_value, max_value):
    if max_value - min_value == 0:
        return 50  # 변화가 없으면 중간값 50을 반환
    return (value - min_value) / (max_value - min_value) * 100

if __name__ == '__main__':
    pass