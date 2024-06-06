from PublicDataReader import TransactionPrice
import requests
import pandas as pd

service_key = ""
api = TransactionPrice(service_key)

#start_year_month
sym="201512"

#end_year_month
eym="202402"

##########################마포
df_mapo = api.get_data(
    property_type="아파트",
    trade_type="매매",
    sigungu_code="11440",
    start_year_month=sym,
    end_year_month=eym,
)
# 필요한 열 선택 및 처리
mapo_selected_df = df_mapo[['지역코드', '년', '월', '전용면적', '거래금액']].copy()
mapo_selected_df['평'] = mapo_selected_df['전용면적'] / 3.3  # 평으로 변환

# 평수 범위 별로 카테고리 설정
bins = [0, 20, 30, 40, 50, float('inf')]  # 평수 범위 정의
labels = ['20평 미만', '20~30평', '30~40평', '40~50평', '50평 이상']
mapo_selected_df['평수 범위'] = pd.cut(mapo_selected_df['평'], bins=bins, labels=labels, right=False)

# 년월 병합
mapo_selected_df.loc[:,'년월'] = mapo_selected_df['년'].astype(str) + mapo_selected_df['월'].astype(str).str.zfill(2)
mapo_selected_df.drop(['년', '월'], axis=1, inplace=True)

# 그룹화 및 데이터 합산
grouped_df = mapo_selected_df.groupby(['년월', '평수 범위'], as_index=False, observed=True).agg({
    '전용면적': 'sum',
    '거래금액': 'sum',
    '지역코드': 'size'
}).rename(columns={'지역코드': '데이터 건수'})

grouped_df['평당 거래금액'] = grouped_df['거래금액'] / grouped_df['전용면적'] * 3.3

# 결과 저장
grouped_df.to_csv("마포_data_summary.csv", index=False)


#########################서대문
df_seodaemoon = api.get_data(
    property_type="아파트",
    trade_type="매매",
    sigungu_code="11410",
    start_year_month=sym,
    end_year_month=eym,
)
# 필요한 열 선택 및 처리
seodaemoon_selected_df = df_seodaemoon[['지역코드', '년', '월', '전용면적', '거래금액']].copy()
seodaemoon_selected_df['평'] = seodaemoon_selected_df['전용면적'] / 3.3  # 평으로 변환

# 평수 범위 별로 카테고리 설정
seodaemoon_selected_df['평수 범위'] = pd.cut(seodaemoon_selected_df['평'], bins=bins, labels=labels, right=False)

# 년월 병합
seodaemoon_selected_df.loc[:,'년월'] = seodaemoon_selected_df['년'].astype(str) + seodaemoon_selected_df['월'].astype(str).str.zfill(2)
seodaemoon_selected_df.drop(['년', '월'], axis=1, inplace=True)

# 그룹화 및 데이터 합산
grouped_df = seodaemoon_selected_df.groupby(['년월', '평수 범위'], as_index=False, observed=True).agg({
    '전용면적': 'sum',
    '거래금액': 'sum',
    '지역코드': 'size'
}).rename(columns={'지역코드': '데이터 건수'})

grouped_df['평당 거래금액'] = grouped_df['거래금액'] / grouped_df['전용면적'] * 3.3

# 결과 저장
grouped_df.to_csv("서대문_data_summary.csv", index=False)


###########################서초
df_seocho = api.get_data(
    property_type="아파트",
    trade_type="매매",
    sigungu_code="11650",
    start_year_month=sym,
    end_year_month=eym,
)
# 필요한 열 선택 및 처리
seocho_selected_df = df_seocho[['지역코드', '년', '월', '전용면적', '거래금액']].copy()
seocho_selected_df['평'] = seocho_selected_df['전용면적'] / 3.3  # 평으로 변환

# 평수 범위 별로 카테고리 설정
seocho_selected_df['평수 범위'] = pd.cut(seocho_selected_df['평'], bins=bins, labels=labels, right=False)

# 년월 병합
seocho_selected_df.loc[:,'년월'] = seocho_selected_df['년'].astype(str) + seocho_selected_df['월'].astype(str).str.zfill(2)
seocho_selected_df.drop(['년', '월'], axis=1, inplace=True)

# 그룹화 및 데이터 합산
grouped_df = seocho_selected_df.groupby(['년월', '평수 범위'], as_index=False, observed=True).agg({
    '전용면적': 'sum',
    '거래금액': 'sum',
    '지역코드': 'size'
}).rename(columns={'지역코드': '데이터 건수'})

grouped_df['평당 거래금액'] = grouped_df['거래금액'] / grouped_df['전용면적'] * 3.3

# 결과 저장
grouped_df.to_csv("서초_data_summary.csv", index=False)


###########################성동
df_seongdong = api.get_data(
    property_type="아파트",
    trade_type="매매",
    sigungu_code="11200",
    start_year_month=sym,
    end_year_month=eym,
)
# 필요한 열 선택 및 처리
seongdong_selected_df = df_seongdong[['지역코드', '년', '월', '전용면적', '거래금액']].copy()
seongdong_selected_df['평'] = seongdong_selected_df['전용면적'] / 3.3  # 평으로 변환

# 평수 범위 별로 카테고리 설정
seongdong_selected_df['평수 범위'] = pd.cut(seongdong_selected_df['평'], bins=bins, labels=labels, right=False)

# 년월 병합
seongdong_selected_df.loc[:,'년월'] = seongdong_selected_df['년'].astype(str) + seongdong_selected_df['월'].astype(str).str.zfill(2)
seongdong_selected_df.drop(['년', '월'], axis=1, inplace=True)

# 그룹화 및 데이터 합산
grouped_df = seongdong_selected_df.groupby(['년월', '평수 범위'], as_index=False, observed=True).agg({
    '전용면적': 'sum',
    '거래금액': 'sum',
    '지역코드': 'size'
}).rename(columns={'지역코드': '데이터 건수'})

grouped_df['평당 거래금액'] = grouped_df['거래금액'] / grouped_df['전용면적'] * 3.3

# 결과 저장
grouped_df.to_csv("성동_data_summary.csv", index=False)


############################성북
df_seongbuk = api.get_data(
    property_type="아파트",
    trade_type="매매",
    sigungu_code="11290",
    start_year_month=sym,
    end_year_month=eym,
)
# 필요한 열 선택 및 처리
seongbuk_selected_df = df_seongbuk[['지역코드', '년', '월', '전용면적', '거래금액']].copy()
seongbuk_selected_df['평'] = seongbuk_selected_df['전용면적'] / 3.3  # 평으로 변환

# 평수 범위 별로 카테고리 설정
seongbuk_selected_df['평수 범위'] = pd.cut(seongbuk_selected_df['평'], bins=bins, labels=labels, right=False)

# 년월 병합
seongbuk_selected_df.loc[:,'년월'] = seongbuk_selected_df['년'].astype(str) + seongbuk_selected_df['월'].astype(str).str.zfill(2)
seongbuk_selected_df.drop(['년', '월'], axis=1, inplace=True)

# 그룹화 및 데이터 합산
grouped_df = seongbuk_selected_df.groupby(['년월', '평수 범위'], as_index=False, observed=True).agg({
    '전용면적': 'sum',
    '거래금액': 'sum',
    '지역코드': 'size'
}).rename(columns={'지역코드': '데이터 건수'})

grouped_df['평당 거래금액'] = grouped_df['거래금액'] / grouped_df['전용면적'] * 3.3

# 결과 저장
grouped_df.to_csv("성북_data_summary.csv", index=False)


############################송파
df_songpa = api.get_data(
    property_type="아파트",
    trade_type="매매",
    sigungu_code="11710",
    start_year_month=sym,
    end_year_month=eym,
)
# 필요한 열 선택 및 처리
songpa_selected_df = df_songpa[['지역코드', '년', '월', '전용면적', '거래금액']].copy()
songpa_selected_df['평'] = songpa_selected_df['전용면적'] / 3.3  # 평으로 변환

# 평수 범위 별로 카테고리 설정
songpa_selected_df['평수 범위'] = pd.cut(songpa_selected_df['평'], bins=bins, labels=labels, right=False)

# 년월 병합
songpa_selected_df.loc[:,'년월'] = songpa_selected_df['년'].astype(str) + songpa_selected_df['월'].astype(str).str.zfill(2)
songpa_selected_df.drop(['년', '월'], axis=1, inplace=True)

# 그룹화 및 데이터 합산
grouped_df = songpa_selected_df.groupby(['년월', '평수 범위'], as_index=False, observed=True).agg({
    '전용면적': 'sum',
    '거래금액': 'sum',
    '지역코드': 'size'
}).rename(columns={'지역코드': '데이터 건수'})

grouped_df['평당 거래금액'] = grouped_df['거래금액'] / grouped_df['전용면적'] * 3.3

# 결과 저장
grouped_df.to_csv("송파_data_summary.csv", index=False)


#############################양천
df_yangcheon = api.get_data(
    property_type="아파트",
    trade_type="매매",
    sigungu_code="11470",
    start_year_month=sym,
    end_year_month=eym,
)
# 필요한 열 선택 및 처리
yangcheon_selected_df = df_yangcheon[['지역코드', '년', '월', '전용면적', '거래금액']].copy()
yangcheon_selected_df['평'] = yangcheon_selected_df['전용면적'] / 3.3  # 평으로 변환

# 평수 범위 별로 카테고리 설정
yangcheon_selected_df['평수 범위'] = pd.cut(yangcheon_selected_df['평'], bins=bins, labels=labels, right=False)

# 년월 병합
yangcheon_selected_df.loc[:,'년월'] = yangcheon_selected_df['년'].astype(str) + yangcheon_selected_df['월'].astype(str).str.zfill(2)
yangcheon_selected_df.drop(['년', '월'], axis=1, inplace=True)

# 그룹화 및 데이터 합산
grouped_df = yangcheon_selected_df.groupby(['년월', '평수 범위'], as_index=False, observed=True).agg({
    '전용면적': 'sum',
    '거래금액': 'sum',
    '지역코드': 'size'
}).rename(columns={'지역코드': '데이터 건수'})

grouped_df['평당 거래금액'] = grouped_df['거래금액'] / grouped_df['전용면적'] * 3.3

# 결과 저장
grouped_df.to_csv("양천_data_summary.csv", index=False)


#############################영등포
df_youngdeungpo = api.get_data(
    property_type="아파트",
    trade_type="매매",
    sigungu_code="11560",
    start_year_month=sym,
    end_year_month=eym,
)
# 필요한 열 선택 및 처리
youngdeungpo_selected_df = df_youngdeungpo[['지역코드', '년', '월', '전용면적', '거래금액']].copy()
youngdeungpo_selected_df['평'] = youngdeungpo_selected_df['전용면적'] / 3.3  # 평으로 변환

# 평수 범위 별로 카테고리 설정
youngdeungpo_selected_df['평수 범위'] = pd.cut(youngdeungpo_selected_df['평'], bins=bins, labels=labels, right=False)

# 년월 병합
youngdeungpo_selected_df.loc[:,'년월'] = youngdeungpo_selected_df['년'].astype(str) + youngdeungpo_selected_df['월'].astype(str).str.zfill(2)
youngdeungpo_selected_df.drop(['년', '월'], axis=1, inplace=True)

# 그룹화 및 데이터 합산
grouped_df = youngdeungpo_selected_df.groupby(['년월', '평수 범위'], as_index=False, observed=True).agg({
    '전용면적': 'sum',
    '거래금액': 'sum',
    '지역코드': 'size'
}).rename(columns={'지역코드': '데이터 건수'})

grouped_df['평당 거래금액'] = grouped_df['거래금액'] / grouped_df['전용면적'] * 3.3

# 결과 저장
grouped_df.to_csv("영등포_data_summary.csv", index=False)


#############################용산
df_youngsan = api.get_data(
    property_type="아파트",
    trade_type="매매",
    sigungu_code="11170",
    start_year_month=sym,
    end_year_month=eym,
)
# 필요한 열 선택 및 처리
youngsan_selected_df = df_youngsan[['지역코드', '년', '월', '전용면적', '거래금액']].copy()
youngsan_selected_df['평'] = youngsan_selected_df['전용면적'] / 3.3  # 평으로 변환

# 평수 범위 별로 카테고리 설정
youngsan_selected_df['평수 범위'] = pd.cut(youngsan_selected_df['평'], bins=bins, labels=labels, right=False)

# 년월 병합
youngsan_selected_df.loc[:,'년월'] = youngsan_selected_df['년'].astype(str) + youngsan_selected_df['월'].astype(str).str.zfill(2)
youngsan_selected_df.drop(['년', '월'], axis=1, inplace=True)

# 그룹화 및 데이터 합산
grouped_df = youngsan_selected_df.groupby(['년월', '평수 범위'], as_index=False, observed=True).agg({
    '전용면적': 'sum',
    '거래금액': 'sum',
    '지역코드': 'size'
}).rename(columns={'지역코드': '데이터 건수'})

grouped_df['평당 거래금액'] = grouped_df['거래금액'] / grouped_df['전용면적'] * 3.3

# 결과 저장
grouped_df.to_csv("용산_data_summary.csv", index=False)


##############################은평
df_eunpyeong = api.get_data(
    property_type="아파트",
    trade_type="매매",
    sigungu_code="11380",
    start_year_month=sym,
    end_year_month=eym,
)
# 필요한 열 선택 및 처리
eunpyeong_selected_df = df_eunpyeong[['지역코드', '년', '월', '전용면적', '거래금액']].copy()
eunpyeong_selected_df['평'] = eunpyeong_selected_df['전용면적'] / 3.3  # 평으로 변환

# 평수 범위 별로 카테고리 설정
eunpyeong_selected_df['평수 범위'] = pd.cut(eunpyeong_selected_df['평'], bins=bins, labels=labels, right=False)

# 년월 병합
eunpyeong_selected_df.loc[:,'년월'] = eunpyeong_selected_df['년'].astype(str) + eunpyeong_selected_df['월'].astype(str).str.zfill(2)
eunpyeong_selected_df.drop(['년', '월'], axis=1, inplace=True)

# 그룹화 및 데이터 합산
grouped_df = eunpyeong_selected_df.groupby(['년월', '평수 범위'], as_index=False, observed=True).agg({
    '전용면적': 'sum',
    '거래금액': 'sum',
    '지역코드': 'size'
}).rename(columns={'지역코드': '데이터 건수'})

grouped_df['평당 거래금액'] = grouped_df['거래금액'] / grouped_df['전용면적'] * 3.3

# 결과 저장
grouped_df.to_csv("은평_data_summary.csv", index=False)


###############################중구
df_junggu = api.get_data(
    property_type="아파트",
    trade_type="매매",
    sigungu_code="11140",
    start_year_month=sym,
    end_year_month=eym,
)
# 필요한 열 선택 및 처리
junggu_selected_df = df_junggu[['지역코드', '년', '월', '전용면적', '거래금액']].copy()
junggu_selected_df['평'] = junggu_selected_df['전용면적'] / 3.3  # 평으로 변환

# 평수 범위 별로 카테고리 설정
junggu_selected_df['평수 범위'] = pd.cut(junggu_selected_df['평'], bins=bins, labels=labels, right=False)

# 년월 병합
junggu_selected_df.loc[:,'년월'] = junggu_selected_df['년'].astype(str) + junggu_selected_df['월'].astype(str).str.zfill(2)
junggu_selected_df.drop(['년', '월'], axis=1, inplace=True)

# 그룹화 및 데이터 합산
grouped_df = junggu_selected_df.groupby(['년월', '평수 범위'], as_index=False, observed=True).agg({
    '전용면적': 'sum',
    '거래금액': 'sum',
    '지역코드': 'size'
}).rename(columns={'지역코드': '데이터 건수'})

grouped_df['평당 거래금액'] = grouped_df['거래금액'] / grouped_df['전용면적'] * 3.3

# 결과 저장
grouped_df.to_csv("중구_data_summary.csv", index=False)


###############################중랑
df_jungrang = api.get_data(
    property_type="아파트",
    trade_type="매매",
    sigungu_code="11260",
    start_year_month=sym,
    end_year_month=eym,
)
# 필요한 열 선택 및 처리
jungrang_selected_df = df_jungrang[['지역코드', '년', '월', '전용면적', '거래금액']].copy()
jungrang_selected_df['평'] = jungrang_selected_df['전용면적'] / 3.3  # 평으로 변환

# 평수 범위 별로 카테고리 설정
jungrang_selected_df['평수 범위'] = pd.cut(jungrang_selected_df['평'], bins=bins, labels=labels, right=False)

# 년월 병합
jungrang_selected_df.loc[:,'년월'] = jungrang_selected_df['년'].astype(str) + jungrang_selected_df['월'].astype(str).str.zfill(2)
jungrang_selected_df.drop(['년', '월'], axis=1, inplace=True)

# 그룹화 및 데이터 합산
grouped_df = jungrang_selected_df.groupby(['년월', '평수 범위'], as_index=False, observed=True).agg({
    '전용면적': 'sum',
    '거래금액': 'sum',
    '지역코드': 'size'
}).rename(columns={'지역코드': '데이터 건수'})

grouped_df['평당 거래금액'] = grouped_df['거래금액'] / grouped_df['전용면적'] * 3.3

# 결과 저장
grouped_df.to_csv("중랑_data_summary.csv", index=False)


