import pandas as pd
import numpy as np

# 엑셀 파일 경로 설정
file_path = '네이버트렌드_부동산검색.xlsx'

# 엑셀 파일 읽기 (필요한 경우 불필요한 행 건너뛰기)
data = pd.read_excel(file_path, skiprows=6)  # 예시로 6행을 건너뜀, 필요한 경우 행 수 조정

# 데이터프레임의 열 이름 확인
print("열 이름:", data.columns)

# '날짜' 열을 datetime 형식으로 변환
data['날짜'] = pd.to_datetime(data['날짜'], format='%Y-%m-%d')

# '날짜' 열의 결측값 제거
data = data.dropna(subset=['날짜'])

# 년월 형태로 변환하여 새로운 열 추가
data['년월'] = data['날짜'].dt.strftime('%Y%m')

# 30일 단위로 그룹화
data['30일_단위'] = (data['날짜'] - data['날짜'].min()).dt.days // 30

# 그룹별로 요약 통계 계산
summary = data.groupby(['년월', '30일_단위']).agg({
    '부동산': ['mean', 'std', 'min', 'max', 'sum']
}).reset_index()

# 컬럼 이름 변경
summary.columns = ['년월', '30일_단위', '검색량_평균', '검색량_표준편차', '검색량_최소', '검색량_최대', '검색량_합계']

# 년월 단위로 데이터프레임을 다시 그룹화 (30일 단위 평균을 년월별로 요약)
monthly_summary = summary.groupby('년월').agg({
    '검색량_평균': 'mean',
    '검색량_최소': 'min',
    '검색량_최대': 'max',
}).reset_index()

# CSV 파일로 저장
output_file_path = '00부동산_검색량_월별_요약.csv'
monthly_summary.to_csv(output_file_path, index=False)

print(f"CSV 파일이 저장되었습니다: {output_file_path}")
