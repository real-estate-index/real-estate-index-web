import pandas as pd
import os

# 현재 파일의 디렉토리 경로
current_dir = os.path.dirname(os.path.abspath(__file__))

# CSV 파일 경로
file_path = os.path.join(current_dir, '..', 'transaction', 'transactions_per_square.csv')

# 데이터 읽기
data = pd.read_csv(file_path)

# 필요한 데이터 추출
data = data[['년월', '표준화된 데이터 건수']]

# JSON 형식으로 변환
data_json = data.to_json(orient='records')

print(data_json)
