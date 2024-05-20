import pandas as pd
import os
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

data_csv = 'data.csv'

# 데이터 받아오기
df_csv = pd.read_csv(data_csv)


# 'DT' 심리지수
# 'PRD_DE' 년월
# 'C1_NM' 지역
# 'LST_CHN_DE' 업데이트 년월일


# 원하는 열들만 뽑은 행렬 만들기
selected_items = df_csv[['DT', 'PRD_DE', 'C1_NM', 'LST_CHN_DE']].copy()

# 'PRD_DE'열을 날짜 형태로 변환
selected_items['PRD_DE'] = pd.to_datetime(selected_items['PRD_DE'], format='%Y%m')



# 전국 단위로 슬라이싱
selected_korea = selected_items[selected_items['C1_NM'] == '전국']
print(selected_korea)

#통계량 출력
#print("전국 단위 통계량")
#print(selected_korea.describe())



# 그래프 크기 설정 (너비, 높이)
#plt.figure(figsize=(550, 200))

# 년월 산점도로 출력하기
#plt.scatter(selected_korea['PRD_DE'], selected_korea['DT'])

# 년월 선 그래프로 출력하기
plt.plot(selected_korea['PRD_DE'], selected_korea['DT'])
plt.title("Nationwide index")



# 산점도
# x축 날짜 포맷 설정
# plt.gca() 현재 활성화된 축(Axis)객체 불러오기
# xaxis 이 축 객체의 x축
# set_major_formatter 함수의 x축 주요 눈금에 대한 표시형식
# mdates.DateFormatter 날짜형식지정
# set_major_locator x축의 주요 눈금의 위치를 결정
# mdates.MonthLocator 주요 눈금이 매달에 위치하도록 설정
#plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
#plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=12))

# x축 눈금 레이블 회전 및 크기 조정
plt.xticks(rotation=45)
plt.tick_params(axis='x', which='major', labelsize=8)


# 보정을 위한 최댓값과 최솟값 추가
max_correction = 170
min_correction = 40

# 새로운 행을 DataFrame 형태로 만들기
new_rows = pd.DataFrame({'DT': [max_correction, min_correction]})

# 기존 DataFrame에 새로운 행(최대, 최소 보정값) 추가
selected_items = pd.concat([selected_items, new_rows], ignore_index=True)

# 결과 확인
selected_items.tail()


plt.show()

# 'DT' 열을 표준화하기 위한 z-점수 표준화 식 적용
mean = selected_items['DT'].mean()
std_dev = selected_items['DT'].std()

#새로운 행 표준화된 심리지수 = 편차 / 표준편차
selected_items['standardized_DT'] = (selected_items['DT'] - mean) / std_dev
df_DT_standarization=pd.DataFrame(selected_items)


#표준화된 standardized_DT 열의 최솟값과 최댓값 찾기
min_val=df_DT_standarization['standardized_DT'].min()
max_val=df_DT_standarization['standardized_DT'].max()

#새로운 최솟값과 최댓값 설정(0,100)
new_min_val=0
new_max_val=100

#정규화 공식사용
normalized_data_DT=((df_DT_standarization['standardized_DT']-min_val)/(max_val - min_val)) * (new_max_val - new_min_val)+new_min_val

df_DT_standarization['normalized_DT']=normalized_data_DT

#저장하기
df_DT_standarization.to_csv('standardized_data.csv',index=False)
