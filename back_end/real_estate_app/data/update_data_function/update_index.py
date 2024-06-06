"""
지역별 fear&greed index를 계산하고 데이터베이스에 저장 및 갱신합니다.
"""

import pandas as pd
import os
import glob
from django.conf import settings
from real_estate_app.models import District, DistrictIndex

def load_and_concatenate_files(directory, region):
    pattern = os.path.join(directory, f"{region}_data_summary간단.csv")
    all_files = glob.glob(pattern)

    if not all_files:
        raise FileNotFoundError(f"No files found for region: {region}")

    df_list = [pd.read_csv(file) for file in all_files]
    combined_df = pd.concat(df_list, ignore_index=True)

    return combined_df

def calculate_min_max_values(df):
    df['price_change'] = df['평당 거래가'].pct_change() * 100
    df['volatility_3m'] = df['price_change'].rolling(window=3).std()
    df['volatility_12m'] = df['price_change'].rolling(window=12).std()
    df['volume_3m'] = df['데이터 건수'].rolling(window=3).mean()
    df['volume_12m'] = df['데이터 건수'].rolling(window=12).mean()
    df['momentum_2m'] = df['price_change'].rolling(window=2).mean() * df['데이터 건수'].rolling(window=2).mean()

    df['volatility_diff'] = df['volatility_3m'] - df['volatility_12m']
    df['volume_diff'] = df['volume_3m'] - df['volume_12m']

    min_max_values = {
        'volatility_diff': (df['volatility_diff'].min(), df['volatility_diff'].max()),
        'volume_diff': (df['volume_diff'].min(), df['volume_diff'].max()),
        'momentum_2m': (df['momentum_2m'].min(), df['momentum_2m'].max())
    }

    return min_max_values

def scale_value(value, min_value, max_value):
    if max_value - min_value == 0:
        return 50
    return (value - min_value) / (max_value - min_value) * 100

def process_real_estate_data(region, input_date, min_max_values, trend_data, psychology_data):
    file_path = os.path.join(directory, 'index_source', 'seoul', f'{region}_data_summary간단.csv')
    real_estate_data = pd.read_csv(file_path)
    real_estate_data['년월'] = pd.to_datetime(real_estate_data['년월'], format='%Y%m')
    real_estate_data.sort_values(by='년월', inplace=True)
    real_estate_data['price_change'] = real_estate_data['평당 거래가'].pct_change() * 100

    input_date = pd.to_datetime(input_date, format='%Y%m')
    target_index = real_estate_data[real_estate_data['년월'] == input_date].index[0]
    window_3m_start = max(0, target_index - 2)
    window_12m_start = max(0, target_index - 11)

    data_3m = real_estate_data.iloc[window_3m_start:target_index + 1].copy()
    data_12m = real_estate_data.iloc[window_12m_start:target_index + 1].copy()
    data_2m = real_estate_data.iloc[max(0, target_index - 1):target_index + 1].copy()

    volatility_3m = data_3m['price_change'].std()
    volatility_12m = data_12m['price_change'].std()
    volume_3m = data_3m['데이터 건수'].mean()
    volume_12m = data_12m['데이터 건수'].mean()

    data_2m['momentum_2m'] = data_2m['price_change'].mean() * data_2m['데이터 건수'].mean()
    momentum_2m = data_2m['momentum_2m'].mean()

    volatility_diff = volatility_3m - volatility_12m
    volume_diff = volume_3m - volume_12m

    scaled_momentum_2m = scale_value(momentum_2m, *min_max_values['momentum_2m'])
    scaled_volatility_diff = scale_value(volatility_diff, *min_max_values['volatility_diff'])
    scaled_volume_diff = scale_value(volume_diff, *min_max_values['volume_diff'])

    weights = {
        'Scaled_Volatility_Diff': 0.125,
        'Scaled_Volume_Diff': 0.125,
        'Scaled_Momentum_2m': 0.35,
        '검색량_평균': 0.15,
        'normalized_DT': 0.25
    }

    filtered_search_trend = trend_data[trend_data['년월'] == input_date.strftime('%Y%m')]
    filtered_psychology = psychology_data[psychology_data['년월'] == input_date.strftime('%Y%m')]

    if not filtered_search_trend.empty and not filtered_psychology.empty:
        filtered_search_trend = filtered_search_trend.reset_index(drop=True)
        filtered_psychology = filtered_psychology.reset_index(drop=True)

        fear_greed_index = (
            scaled_volatility_diff * weights['Scaled_Volatility_Diff'] +
            scaled_volume_diff * weights['Scaled_Volume_Diff'] +
            scaled_momentum_2m * weights['Scaled_Momentum_2m'] +
            filtered_search_trend['검색량_평균'][0] * weights['검색량_평균'] +
            filtered_psychology['normalized_DT'][0] * weights['normalized_DT']
        )

        summary = {
            "year_month": input_date.strftime('%Y%m'),
            "fear_greed_index": fear_greed_index
        }

        return summary
    else:
        return None

def update_district_data(directory, trend_csv, psychology_csv):
    regions = [os.path.splitext(f)[0].replace('_data_summary간단', '') for f in os.listdir(os.path.join(directory, 'index_source', 'seoul')) if f.endswith('_data_summary간단.csv')]
    
    for region in regions:
        combined_df = load_and_concatenate_files(os.path.join(directory, 'index_source', 'seoul'), region)
        min_max_values = calculate_min_max_values(combined_df)
        
        trend_data = pd.read_csv(trend_csv)
        trend_data['년월'] = trend_data['년월'].astype(str)
        
        psychology_data = pd.read_csv(psychology_csv)
        psychology_data = psychology_data[psychology_data['C1_NM'] == '서울특별시']
        psychology_data['년월'] = pd.to_datetime(psychology_data['PRD_DE'], format='%Y-%m-%d').dt.strftime('%Y%m')
        
        date_range = pd.date_range(start='2015-12-01', end='2024-02-01', freq='MS').strftime('%Y%m').tolist()

        for date in date_range:
            summary = process_real_estate_data(region, date, min_max_values, trend_data, psychology_data)
            if summary:
                district, created = District.objects.get_or_create(name=region, defaults={'district_id': region})
                DistrictIndex.objects.update_or_create(
                    district=district,
                    year_month=summary['year_month'],
                    defaults={
                        'fear_greed_index': summary['fear_greed_index']
                    }
                )

if __name__ == "__main__":
    directory = os.path.dirname(os.path.abspath(__file__))
    trend_csv = os.path.join(directory, '..', 'index_source', '00부동산_검색량_월별_요약.csv')
    psychology_csv = os.path.join(directory, '..', 'mind', 'mind_standard_data.csv')

    update_district_data(directory, trend_csv, psychology_csv)
