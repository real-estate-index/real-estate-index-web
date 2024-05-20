import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 데이터 로드
fear_greed_data = pd.read_csv('fear_greed_index_full.csv')
price_data = pd.read_csv('강남_data_summary간단.csv')

# '년월' 형식을 맞추기 위해 변환
fear_greed_data['년월'] = pd.to_datetime(fear_greed_data['년월'], format='%Y%m').dt.to_period('M').dt.to_timestamp()
price_data['년월'] = pd.to_datetime(price_data['년월'], format='%Y%m')

# 데이터 병합
merged_data = pd.merge(fear_greed_data, price_data, on='년월', how='inner')

# 상관관계 분석
correlation_matrix = merged_data[['fear_greed_index', '평당 거래가']].corr()

print("상관관계 분석 결과:")
print(correlation_matrix)

# 시각화
plt.figure(figsize=(14, 7))

# 공포탐욕지수와 가격의 시계열 그래프
plt.subplot(2, 1, 1)
plt.plot(merged_data['년월'], merged_data['fear_greed_index'], label='Fear and Greed Index', color='blue')
plt.ylabel('Fear and Greed Index')
plt.legend(loc='upper left')
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(merged_data['년월'], merged_data['평당 거래가'], label='Price per Unit Area', color='red')
plt.xlabel('Date')
plt.ylabel('Price per Unit Area')
plt.legend(loc='upper left')
plt.grid(True)

plt.tight_layout()
plt.show()

# 공포탐욕지수와 가격의 산점도
plt.figure(figsize=(7, 7))
sns.scatterplot(x='fear_greed_index', y='평당 거래가', data=merged_data)
plt.xlabel('Fear and Greed Index')
plt.ylabel('Price per Unit Area')
plt.title('Scatter plot between Fear and Greed Index and Price per Unit Area')
plt.grid(True)
plt.show()
