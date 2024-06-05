from PublicDataReader import TransactionPrice
import requests
import pandas as pd

service_key = ""
api = TransactionPrice(service_key)

#start_year_month
sym="201512"

#end_year_month
eym="202402"

# 기간 내 조회
####################종로
df_jonglo = api.get_data(
    property_type="아파트",
    trade_type="매매",
    sigungu_code="11110",
    start_year_month=sym,
    end_year_month=eym,
)
#원본저장
df_jonglo.to_csv("0_원본데이터(종로).csv", index=False)

#필요한 열 선택 및 처리
jonglo_selected_df = df_jonglo[['지역코드', '년', '월', '전용면적', '거래금액']].copy()
jonglo_selected_df['평'] = jonglo_selected_df['전용면적'] / 3.3  # 평으로 변환

# 평수 범위별로 카테고리 설정
bins = [0, 20, 30, 40, 50, float('inf')]  # 평수 범위 정의
labels = ['20평 미만', '20~30평', '30~40평', '40~50평', '50평 이상']
jonglo_selected_df['평수 범위'] = pd.cut(jonglo_selected_df['평'], bins=bins, labels=labels, right=False)

#년월 병합
jonglo_selected_df.loc[:,'년월'] = jonglo_selected_df['년'].astype(str) + jonglo_selected_df['월'].astype(str).str.zfill(2)
jonglo_selected_df.drop(['년', '월'], axis=1, inplace=True)

#그룹화 및 데이터 합산
# 그룹화 및 데이터 합산
grouped_df = jonglo_selected_df.groupby(['년월', '평수 범위'], as_index=False, observed=True).agg({
    '전용면적': 'sum',
    '거래금액': 'sum',
    '지역코드': 'size'
}).rename(columns={'지역코드': '데이터 건수'})

grouped_df['평당 거래금액'] = grouped_df['거래금액'] / grouped_df['전용면적'] * 3.3

#결과 저장
grouped_df.to_csv("종로_data_summary.csv", index=False)


#######################강남
df_gangnam = api.get_data(
    property_type="아파트",
    trade_type="매매",
    sigungu_code="11680",
    start_year_month=sym,
    end_year_month=eym,
)

#필요한 열 선택 및 처리
gangnam_selected_df = df_gangnam[['지역코드', '년', '월', '전용면적', '거래금액']].copy()
gangnam_selected_df['평'] = gangnam_selected_df['전용면적'] / 3.3  # 평으로 변환

# 평수 범위 별로 카테고리 설정
gangnam_selected_df['평수 범위'] = pd.cut(gangnam_selected_df['평'], bins=bins, labels=labels, right=False)

#년월 병합
gangnam_selected_df.loc[:,'년월'] = gangnam_selected_df['년'].astype(str) + gangnam_selected_df['월'].astype(str).str.zfill(2)
gangnam_selected_df.drop(['년', '월'], axis=1, inplace=True)

# 그룹화 및 데이터 합산
grouped_df = gangnam_selected_df.groupby(['년월', '평수 범위'], as_index=False, observed=True).agg({
    '전용면적': 'sum',
    '거래금액': 'sum',
    '지역코드': 'size'
}).rename(columns={'지역코드': '데이터 건수'})

grouped_df['평당 거래금액'] = grouped_df['거래금액'] / grouped_df['전용면적'] * 3.3

#결과 저장
grouped_df.to_csv("강남_data_summary.csv", index=False)

######################강동
df_gangdong = api.get_data(
    property_type="아파트",
    trade_type="매매",
    sigungu_code="11740",
    start_year_month=sym,
    end_year_month=eym,
)

# 필요한 열 선택 및 처리
gangdong_selected_df = df_gangdong[['지역코드', '년', '월', '전용면적', '거래금액']].copy()
gangdong_selected_df['평'] = gangdong_selected_df['전용면적'] / 3.3  # 평으로 변환

# 평수 범위 별로 카테고리 설정
gangdong_selected_df['평수 범위'] = pd.cut(gangdong_selected_df['평'], bins=bins, labels=labels, right=False)

# 년월 병합
gangdong_selected_df.loc[:,'년월'] = gangdong_selected_df['년'].astype(str) + gangdong_selected_df['월'].astype(str).str.zfill(2)
gangdong_selected_df.drop(['년', '월'], axis=1, inplace=True)

# 그룹화 및 데이터 합산
grouped_df = gangdong_selected_df.groupby(['년월', '평수 범위'], as_index=False, observed=True).agg({
    '전용면적': 'sum',
    '거래금액': 'sum',
    '지역코드': 'size'
}).rename(columns={'지역코드': '데이터 건수'})

grouped_df['평당 거래금액'] = grouped_df['거래금액'] / grouped_df['전용면적'] * 3.3

# 결과 저장
grouped_df.to_csv("강동_data_summary.csv", index=False)

#####################강북
df_gangbuk = api.get_data(
    property_type="아파트",
    trade_type="매매",
    sigungu_code="11305",
    start_year_month=sym,
    end_year_month=eym,
)
# 필요한 열 선택 및 처리
gangbuk_selected_df = df_gangbuk[['지역코드', '년', '월', '전용면적', '거래금액']].copy()
gangbuk_selected_df['평'] = gangbuk_selected_df['전용면적'] / 3.3  # 평으로 변환

# 평수 범위 별로 카테고리 설정
gangbuk_selected_df['평수 범위'] = pd.cut(gangbuk_selected_df['평'], bins=bins, labels=labels, right=False)

# 년월 병합
gangbuk_selected_df.loc[:,'년월'] = gangbuk_selected_df['년'].astype(str) + gangbuk_selected_df['월'].astype(str).str.zfill(2)
gangbuk_selected_df.drop(['년', '월'], axis=1, inplace=True)

# 그룹화 및 데이터 합산
grouped_df = gangbuk_selected_df.groupby(['년월', '평수 범위'], as_index=False, observed=True).agg({
    '전용면적': 'sum',
    '거래금액': 'sum',
    '지역코드': 'size'
}).rename(columns={'지역코드': '데이터 건수'})

grouped_df['평당 거래금액'] = grouped_df['거래금액'] / grouped_df['전용면적'] * 3.3

# 결과 저장
grouped_df.to_csv("강북_data_summary.csv", index=False)


###################강서
df_gangseo = api.get_data(
    property_type="아파트",
    trade_type="매매",
    sigungu_code="11500",
    start_year_month=sym,
    end_year_month=eym,
)
# 필요한 열 선택 및 처리
gangseo_selected_df = df_gangseo[['지역코드', '년', '월', '전용면적', '거래금액']].copy()
gangseo_selected_df['평'] = gangseo_selected_df['전용면적'] / 3.3  # 평으로 변환

# 평수 범위 별로 카테고리 설정
gangseo_selected_df['평수 범위'] = pd.cut(gangseo_selected_df['평'], bins=bins, labels=labels, right=False)

# 년월 병합
gangseo_selected_df.loc[:,'년월'] = gangseo_selected_df['년'].astype(str) + gangseo_selected_df['월'].astype(str).str.zfill(2)
gangseo_selected_df.drop(['년', '월'], axis=1, inplace=True)

# 그룹화 및 데이터 합산
grouped_df = gangseo_selected_df.groupby(['년월', '평수 범위'], as_index=False, observed=True).agg({
    '전용면적': 'sum',
    '거래금액': 'sum',
    '지역코드': 'size'
}).rename(columns={'지역코드': '데이터 건수'})

grouped_df['평당 거래금액'] = grouped_df['거래금액'] / grouped_df['전용면적'] * 3.3

# 결과 저장
grouped_df.to_csv("강서_data_summary.csv", index=False)


#################관악
df_gwanak = api.get_data(
    property_type="아파트",
    trade_type="매매",
    sigungu_code="11620",
    start_year_month=sym,
    end_year_month=eym,
)
# 필요한 열 선택 및 처리
gwanak_selected_df = df_gwanak[['지역코드', '년', '월', '전용면적', '거래금액']].copy()
gwanak_selected_df['평'] = gwanak_selected_df['전용면적'] / 3.3  # 평으로 변환

# 평수 범위 별로 카테고리 설정
gwanak_selected_df['평수 범위'] = pd.cut(gwanak_selected_df['평'], bins=bins, labels=labels, right=False)

# 년월 병합
gwanak_selected_df.loc[:,'년월'] = gwanak_selected_df['년'].astype(str) + gwanak_selected_df['월'].astype(str).str.zfill(2)
gwanak_selected_df.drop(['년', '월'], axis=1, inplace=True)

# 그룹화 및 데이터 합산
grouped_df = gwanak_selected_df.groupby(['년월', '평수 범위'], as_index=False, observed=True).agg({
    '전용면적': 'sum',
    '거래금액': 'sum',
    '지역코드': 'size'
}).rename(columns={'지역코드': '데이터 건수'})

grouped_df['평당 거래금액'] = grouped_df['거래금액'] / grouped_df['전용면적'] * 3.3

# 결과 저장
grouped_df.to_csv("관악_data_summary.csv", index=False)


#########################광진
df_gwangjin = api.get_data(
    property_type="아파트",
    trade_type="매매",
    sigungu_code="11215",
    start_year_month=sym,
    end_year_month=eym,
)
# 필요한 열 선택 및 처리
gwangjin_selected_df = df_gwangjin[['지역코드', '년', '월', '전용면적', '거래금액']].copy()
gwangjin_selected_df['평'] = gwangjin_selected_df['전용면적'] / 3.3  # 평으로 변환

# 평수 범위 별로 카테고리 설정
gwangjin_selected_df['평수 범위'] = pd.cut(gwangjin_selected_df['평'], bins=bins, labels=labels, right=False)

# 년월 병합
gwangjin_selected_df.loc[:,'년월'] = gwangjin_selected_df['년'].astype(str) + gwangjin_selected_df['월'].astype(str).str.zfill(2)
gwangjin_selected_df.drop(['년', '월'], axis=1, inplace=True)

# 그룹화 및 데이터 합산
grouped_df = gwangjin_selected_df.groupby(['년월', '평수 범위'], as_index=False, observed=True).agg({
    '전용면적': 'sum',
    '거래금액': 'sum',
    '지역코드': 'size'
}).rename(columns={'지역코드': '데이터 건수'})

grouped_df['평당 거래금액'] = grouped_df['거래금액'] / grouped_df['전용면적'] * 3.3

# 결과 저장
grouped_df.to_csv("광진_data_summary.csv", index=False)


#######################구로
df_guro = api.get_data(
    property_type="아파트",
    trade_type="매매",
    sigungu_code="11530",
    start_year_month=sym,
    end_year_month=eym,
)
# 필요한 열 선택 및 처리
guro_selected_df = df_guro[['지역코드', '년', '월', '전용면적', '거래금액']].copy()
guro_selected_df['평'] = guro_selected_df['전용면적'] / 3.3  # 평으로 변환

# 평수 범위 별로 카테고리 설정
guro_selected_df['평수 범위'] = pd.cut(guro_selected_df['평'], bins=bins, labels=labels, right=False)

# 년월 병합
guro_selected_df.loc[:,'년월'] = guro_selected_df['년'].astype(str) + guro_selected_df['월'].astype(str).str.zfill(2)
guro_selected_df.drop(['년', '월'], axis=1, inplace=True)

# 그룹화 및 데이터 합산
grouped_df = guro_selected_df.groupby(['년월', '평수 범위'], as_index=False, observed=True).agg({
    '전용면적': 'sum',
    '거래금액': 'sum',
    '지역코드': 'size'
}).rename(columns={'지역코드': '데이터 건수'})

grouped_df['평당 거래금액'] = grouped_df['거래금액'] / grouped_df['전용면적'] * 3.3

# 결과 저장
grouped_df.to_csv("구로_data_summary.csv", index=False)


