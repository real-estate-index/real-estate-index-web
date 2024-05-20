import pandas as pd
import os
import glob

def load_and_concatenate_files(directory, region):
    # 특정 지역의 CSV 파일 경로를 읽어옴
    pattern = os.path.join(directory, f"{region}_data_summary간단.csv")
    all_files = glob.glob(pattern)

    # 파일 데이터가 존재하지 않는 경우 처리
    if not all_files:
        raise FileNotFoundError(f"No files found for region: {region}")

    # 파일 데이터를 하나의 데이터프레임으로 결합
    df_list = [pd.read_csv(file) for file in all_files]
    combined_df = pd.concat(df_list, ignore_index=True)

    return combined_df

def calculate_min_max_values(df):
    # 일별 가격 변화율 (퍼센트 변화) 계산
    df['price_change'] = df['평당 거래가'].pct_change() * 100

    # 변동성, 거래량, 모멘텀 계산을 위해 rolling 적용
    df['volatility_3m'] = df['price_change'].rolling(window=3).std()
    df['volatility_12m'] = df['price_change'].rolling(window=12).std()
    df['volume_3m'] = df['데이터 건수'].rolling(window=3).mean()
    df['volume_12m'] = df['데이터 건수'].rolling(window=12).mean()
    df['momentum_2m'] = df['price_change'].rolling(window=2).mean() * df['데이터 건수'].rolling(window=2).mean()

    # 3개월과 12개월 지표의 차이 계산
    df['volatility_diff'] = df['volatility_3m'] - df['volatility_12m']
    df['volume_diff'] = df['volume_3m'] - df['volume_12m']

    # 각 차이의 절대값을 사용하여 최소값과 최대값 계산
    min_max_values = {
        'volatility_diff': (df['volatility_diff'].min(), df['volatility_diff'].max()),
        'volume_diff': (df['volume_diff'].min(), df['volume_diff'].max()),
        'momentum_2m': (df['momentum_2m'].min(), df['momentum_2m'].max())
    }

    return min_max_values

def scale_value(value, min_value, max_value):
    # Min-Max Scaling을 사용하여 값을 0~100으로 변환
    if max_value - min_value == 0:
        return 50  # 변화가 없으면 중간값 50을 반환
    return (value - min_value) / (max_value - min_value) * 100

def process_real_estate_data(region, input_date, min_max_values):
    # 파일 경로 설정
    file_path = f'{region}_data_summary간단.csv'

    # CSV 파일 로드
    real_estate_data = pd.read_csv(file_path)

    # '년월' 열을 datetime 형식으로 변환
    real_estate_data['년월'] = pd.to_datetime(real_estate_data['년월'], format='%Y%m')

    # '년월' 기준으로 정렬
    real_estate_data.sort_values(by='년월', inplace=True)

    # 일별 가격 변화율 (퍼센트 변화) 계산
    real_estate_data['price_change'] = real_estate_data['평당 거래가'].pct_change() * 100

    # 특정 년월을 입력받음
    input_date = pd.to_datetime(input_date, format='%Y%m')

    # 입력된 년월을 기준으로 데이터 필터링
    target_index = real_estate_data[real_estate_data['년월'] == input_date].index[0]

    # 입력된 년월을 기준으로 3개월 및 12개월 데이터를 추출
    window_3m_start = max(0, target_index - 2)
    window_12m_start = max(0, target_index - 11)

    # 3개월(3행) 및 12개월(12행) 데이터 추출
    data_3m = real_estate_data.iloc[window_3m_start:target_index + 1].copy()
    data_12m = real_estate_data.iloc[window_12m_start:target_index + 1].copy()
    data_2m = real_estate_data.iloc[max(0, target_index - 1):target_index + 1].copy()

    # 3개월(3행) 및 12개월(12행) 이동 변동성 계산
    volatility_3m = data_3m['price_change'].std()
    volatility_12m = data_12m['price_change'].std()

    # 3개월(3행) 및 12개월(12행) 평균 거래량 계산
    volume_3m = data_3m['데이터 건수'].mean()
    volume_12m = data_12m['데이터 건수'].mean()

    # 모멘텀 계산 (가격 변화와 거래량의 곱)
    data_2m.loc[:, 'momentum_2m'] = data_2m['price_change'].mean() * data_2m['데이터 건수'].mean()
    momentum_2m = data_2m['momentum_2m'].mean()

    # 지표의 차이 계산
    volatility_diff = volatility_3m - volatility_12m
    volume_diff = volume_3m - volume_12m

    # 모멘텀 스케일링
    scaled_momentum_2m = scale_value(momentum_2m, *min_max_values['momentum_2m'])

    # 각 차이를 0~100 사이로 변환
    scaled_volatility_diff = scale_value(volatility_diff, *min_max_values['volatility_diff'])
    scaled_volume_diff = scale_value(volume_diff, *min_max_values['volume_diff'])

    # 전월 대비 가격 변화율 계산
    if target_index > 0:
        price_change_1m = (real_estate_data.iloc[target_index]['평당 거래가'] - real_estate_data.iloc[target_index - 1]['평당 거래가']) / real_estate_data.iloc[target_index - 1]['평당 거래가'] * 100
    else:
        price_change_1m = None

    # 3개월 대비 가격 변화율 계산
    if target_index >= 2:
        price_change_3m = (real_estate_data.iloc[target_index]['평당 거래가'] - real_estate_data.iloc[target_index - 3]['평당 거래가']) / real_estate_data.iloc[target_index - 3]['평당 거래가'] * 100
    else:
        price_change_3m = None

    # 1년 대비 가격 변화율 계산
    if target_index >= 11:
        price_change_12m = (real_estate_data.iloc[target_index]['평당 거래가'] - real_estate_data.iloc[target_index - 12]['평당 거래가']) / real_estate_data.iloc[target_index - 12]['평당 거래가'] * 100
    else:
        price_change_12m = None

    # 결과 요약
    summary = {
        "년월": input_date.strftime('%Y%m'),  # '년월' 열 추가
        "Date": input_date,
        "Volatility_3m": volatility_3m,
        "Volatility_12m": volatility_12m,
        "Volume_3m": volume_3m,
        "Volume_12m": volume_12m,
        "Momentum_2m": momentum_2m,
        "Volatility_Diff": volatility_diff,
        "Volume_Diff": volume_diff,
        "Scaled_Volatility_Diff": scaled_volatility_diff,
        "Scaled_Volume_Diff": scaled_volume_diff,
        "Scaled_Momentum_2m": scaled_momentum_2m,
        "Price_Change_1m": price_change_1m,
        "Price_Change_3m": price_change_3m,
        "Price_Change_12m": price_change_12m
    }

    # 결과 출력
    summary_df = pd.DataFrame([summary])

    # pandas 출력 옵션 설정
    pd.set_option('display.max_columns', None)  # 모든 열 출력
    pd.set_option('display.width', None)  # 출력 너비 설정 (화면 크기에 맞게)

    return summary_df

# 모든 파일 로드 및 결합
directory = ''
region = input("지역을 입력해주세요 (ex)강남, 강서) >> ")  # 입력 지역
combined_df = load_and_concatenate_files(directory, region)

# 각 지표의 최소값과 최대값 계산
min_max_values = calculate_min_max_values(combined_df)

# 특정 년월의 데이터를 기준으로 지표 계산
input_date = input("년월을 입력해주세요 (ex)202112) >> ")  # 입력 날짜

# 결과 출력



real_estate_summary = process_real_estate_data(region, input_date, min_max_values)

### 부동산 검색량
trend_csv = '00부동산_검색량_월별_요약.csv'
df_trend = pd.read_csv(trend_csv)
df_trend['년월'] = df_trend['년월'].astype(str)  # '년월' 열을 문자열로 변환
search_trend_data = df_trend[['년월', '검색량_평균']]

### 심리지수
df_psychology = pd.read_csv("standardized_data.csv")

df_psychology = df_psychology[df_psychology['C1_NM'] == '서울특별시']  # '서울특별시' 행들만 필터링
df_psychology['년월'] = pd.to_datetime(df_psychology['PRD_DE'], format='%Y-%m-%d').dt.strftime('%Y%m')
psychology_data = df_psychology[['년월', 'normalized_DT']]

# 검색량 데이터에서 해당 년월의 데이터 필터링
filtered_search_trend = search_trend_data[search_trend_data['년월'] == real_estate_summary.iloc[0]['년월']]

# 심리지수 데이터에서 해당 년월의 데이터 필터링
filtered_psychology = psychology_data[psychology_data['년월'] == real_estate_summary.iloc[0]['년월']]

# 필터링된 데이터 확인
print(filtered_search_trend)
print(filtered_psychology)

# 데이터 병합
merged_data = pd.merge(real_estate_summary, filtered_search_trend, on='년월')
merged_data = pd.merge(merged_data, filtered_psychology, on='년월')

# 가중치 설정
weights = {
    'Scaled_Volatility_Diff': 0.125,
    'Scaled_Volume_Diff': 0.125,
    'Scaled_Momentum_2m': 0.35,
    '검색량_평균': 0.15,
    'normalized_DT': 0.25
}

# 가중 평균을 계산하여 fear_greed_index 생성
merged_data['fear_greed_index'] = (
    merged_data['Scaled_Volatility_Diff'] * weights['Scaled_Volatility_Diff'] +
    merged_data['Scaled_Volume_Diff'] * weights['Scaled_Volume_Diff'] +
    merged_data['Scaled_Momentum_2m'] * weights['Scaled_Momentum_2m'] +
    merged_data['검색량_평균'] * weights['검색량_평균'] +
    merged_data['normalized_DT'] * weights['normalized_DT']
)

# 최종 데이터 출력
print("Final Merged Data with Fear and Greed Index:")
print(merged_data)


# 최종 데이터 CSV 파일로 저장
output_file_path = 'fear_greed_index.csv'
merged_data.to_csv(output_file_path, index=False)

print(f"최종 종합 데이터가 저장되었습니다: {output_file_path}")



#### 기간 설정
start_date = '2015-12-01'
end_date = '2024-02-01'
date_range = pd.date_range(start=start_date, end=end_date, freq='MS').strftime('%Y%m').tolist()

# 결과를 저장할 데이터프레임 초기화
final_results = pd.DataFrame()

for date in date_range:
    try:
        real_estate_summary = process_real_estate_data(region, date, min_max_values)

        # 특정 년월의 검색량 데이터와 심리지수 데이터 필터링
        filtered_search_trend = search_trend_data[search_trend_data['년월'] == real_estate_summary.iloc[0]['년월']]
        filtered_psychology = psychology_data[psychology_data['년월'] == real_estate_summary.iloc[0]['년월']]

        if not filtered_search_trend.empty and not filtered_psychology.empty:
            # 인덱스 맞추기
            filtered_search_trend = filtered_search_trend.reset_index(drop=True)
            filtered_psychology = filtered_psychology.reset_index(drop=True)
            real_estate_summary = real_estate_summary.reset_index(drop=True)

            # 데이터 병합
            merged_data = pd.merge(real_estate_summary, filtered_search_trend, on='년월')
            merged_data = pd.merge(merged_data, filtered_psychology, on='년월')

            # 가중 평균을 계산하여 fear_greed_index 생성
            merged_data['fear_greed_index'] = (
                    merged_data['Scaled_Volatility_Diff'] * weights['Scaled_Volatility_Diff'] +
                    merged_data['Scaled_Volume_Diff'] * weights['Scaled_Volume_Diff'] +
                    merged_data['Scaled_Momentum_2m'] * weights['Scaled_Momentum_2m'] +
                    merged_data['검색량_평균'] * weights['검색량_평균'] +
                    merged_data['normalized_DT'] * weights['normalized_DT']
            )

            # 결과 추가
            if not merged_data.empty:
                final_results = pd.concat([final_results, merged_data], ignore_index=True)
    except Exception as e:
        print(f"Error processing date {date}: {e}")

# 최종 데이터 CSV 파일로 저장
output_file_path = 'fear_greed_index_full.csv'
final_results.to_csv(output_file_path, index=False)

print(f"최종 종합 데이터가 저장되었습니다: {output_file_path}")

