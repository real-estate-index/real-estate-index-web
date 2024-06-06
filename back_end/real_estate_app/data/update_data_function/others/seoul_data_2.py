from PublicDataReader import TransactionPrice
import requests
import pandas as pd

service_key = ""
api = TransactionPrice(service_key)

#start_year_month
sym="201512"

#end_year_month
eym="202402"



######################금천
df_gumcheon = api.get_data(
    property_type="아파트",
    trade_type="매매",
    sigungu_code="11545",
    start_year_month=sym,
    end_year_month=eym,
)
# 필요한 열 선택 및 처리
gumcheon_selected_df = df_gumcheon[['지역코드', '년', '월', '전용면적', '거래금액']].copy()
gumcheon_selected_df['평'] = gumcheon_selected_df['전용면적'] / 3.3  # 평으로 변환

# 평수 범위 별로 카테고리 설정
bins = [0, 20, 30, 40, 50, float('inf')]  # 평수 범위 정의
labels = ['20평 미만', '20~30평', '30~40평', '40~50평', '50평 이상']
gumcheon_selected_df['평수 범위'] = pd.cut(gumcheon_selected_df['평'], bins=bins, labels=labels, right=False)

# 년월 병합
gumcheon_selected_df.loc[:,'년월'] = gumcheon_selected_df['년'].astype(str) + gumcheon_selected_df['월'].astype(str).str.zfill(2)
gumcheon_selected_df.drop(['년', '월'], axis=1, inplace=True)

# 그룹화 및 데이터 합산
grouped_df = gumcheon_selected_df.groupby(['년월', '평수 범위'], as_index=False, observed=True).agg({
    '전용면적': 'sum',
    '거래금액': 'sum',
    '지역코드': 'size'
}).rename(columns={'지역코드': '데이터 건수'})

grouped_df['평당 거래금액'] = grouped_df['거래금액'] / grouped_df['전용면적'] * 3.3

# 결과 저장
grouped_df.to_csv("금천_data_summary.csv", index=False)


#######################노원
df_noone = api.get_data(
    property_type="아파트",
    trade_type="매매",
    sigungu_code="11350",
    start_year_month=sym,
    end_year_month=eym,
)
# 필요한 열 선택 및 처리
noone_selected_df = df_noone[['지역코드', '년', '월', '전용면적', '거래금액']].copy()
noone_selected_df['평'] = noone_selected_df['전용면적'] / 3.3  # 평으로 변환

# 평수 범위 별로 카테고리 설정
noone_selected_df['평수 범위'] = pd.cut(noone_selected_df['평'], bins=bins, labels=labels, right=False)

# 년월 병합
noone_selected_df.loc[:,'년월'] = noone_selected_df['년'].astype(str) + noone_selected_df['월'].astype(str).str.zfill(2)
noone_selected_df.drop(['년', '월'], axis=1, inplace=True)

# 그룹화 및 데이터 합산
grouped_df = noone_selected_df.groupby(['년월', '평수 범위'], as_index=False, observed=True).agg({
    '전용면적': 'sum',
    '거래금액': 'sum',
    '지역코드': 'size'
}).rename(columns={'지역코드': '데이터 건수'})

grouped_df['평당 거래금액'] = grouped_df['거래금액'] / grouped_df['전용면적'] * 3.3

# 결과 저장
grouped_df.to_csv("노원_data_summary.csv", index=False)


########################도봉
df_dobong = api.get_data(
    property_type="아파트",
    trade_type="매매",
    sigungu_code="11320",
    start_year_month=sym,
    end_year_month=eym,
)
# 필요한 열 선택 및 처리
dobong_selected_df = df_dobong[['지역코드', '년', '월', '전용면적', '거래금액']].copy()
dobong_selected_df['평'] = dobong_selected_df['전용면적'] / 3.3  # 평으로 변환

# 평수 범위 별로 카테고리 설정
dobong_selected_df['평수 범위'] = pd.cut(dobong_selected_df['평'], bins=bins, labels=labels, right=False)

# 년월 병합
dobong_selected_df.loc[:,'년월'] = dobong_selected_df['년'].astype(str) + dobong_selected_df['월'].astype(str).str.zfill(2)
dobong_selected_df.drop(['년', '월'], axis=1, inplace=True)

# 그룹화 및 데이터 합산
grouped_df = dobong_selected_df.groupby(['년월', '평수 범위'], as_index=False, observed=True).agg({
    '전용면적': 'sum',
    '거래금액': 'sum',
    '지역코드': 'size'
}).rename(columns={'지역코드': '데이터 건수'})

grouped_df['평당 거래금액'] = grouped_df['거래금액'] / grouped_df['전용면적'] * 3.3

# 결과 저장
grouped_df.to_csv("도봉_data_summary.csv", index=False)

##########################동대문
df_dongdaemoon = api.get_data(
    property_type="아파트",
    trade_type="매매",
    sigungu_code="11230",
    start_year_month=sym,
    end_year_month=eym,
)
# 필요한 열 선택 및 처리
dongdaemoon_selected_df = df_dongdaemoon[['지역코드', '년', '월', '전용면적', '거래금액']].copy()
dongdaemoon_selected_df['평'] = dongdaemoon_selected_df['전용면적'] / 3.3  # 평으로 변환

# 평수 범위 별로 카테고리 설정
dongdaemoon_selected_df['평수 범위'] = pd.cut(dongdaemoon_selected_df['평'], bins=bins, labels=labels, right=False)

# 년월 병합
dongdaemoon_selected_df.loc[:,'년월'] = dongdaemoon_selected_df['년'].astype(str) + dongdaemoon_selected_df['월'].astype(str).str.zfill(2)
dongdaemoon_selected_df.drop(['년', '월'], axis=1, inplace=True)

# 그룹화 및 데이터 합산
grouped_df = dongdaemoon_selected_df.groupby(['년월', '평수 범위'], as_index=False, observed=True).agg({
    '전용면적': 'sum',
    '거래금액': 'sum',
    '지역코드': 'size'
}).rename(columns={'지역코드': '데이터 건수'})

grouped_df['평당 거래금액'] = grouped_df['거래금액'] / grouped_df['전용면적'] * 3.3

# 결과 저장
grouped_df.to_csv("동대문_data_summary.csv", index=False)


###########################동작
df_dongjak = api.get_data(
    property_type="아파트",
    trade_type="매매",
    sigungu_code="11590",
    start_year_month=sym,
    end_year_month=eym,
)
# 필요한 열 선택 및 처리
dongjak_selected_df = df_dongjak[['지역코드', '년', '월', '전용면적', '거래금액']].copy()
dongjak_selected_df['평'] = dongjak_selected_df['전용면적'] / 3.3  # 평으로 변환

# 평수 범위 별로 카테고리 설정
dongjak_selected_df['평수 범위'] = pd.cut(dongjak_selected_df['평'], bins=bins, labels=labels, right=False)

# 년월 병합
dongjak_selected_df.loc[:,'년월'] = dongjak_selected_df['년'].astype(str) + dongjak_selected_df['월'].astype(str).str.zfill(2)
dongjak_selected_df.drop(['년', '월'], axis=1, inplace=True)

# 그룹화 및 데이터 합산
grouped_df = dongjak_selected_df.groupby(['년월', '평수 범위'], as_index=False, observed=True).agg({
    '전용면적': 'sum',
    '거래금액': 'sum',
    '지역코드': 'size'
}).rename(columns={'지역코드': '데이터 건수'})

grouped_df['평당 거래금액'] = grouped_df['거래금액'] / grouped_df['전용면적'] * 3.3

# 결과 저장
grouped_df.to_csv("동작_data_summary.csv", index=False)


