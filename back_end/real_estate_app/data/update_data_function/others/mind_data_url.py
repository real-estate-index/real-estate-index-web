import requests
import pandas as pd
import openpyxl

url="your key"
r=requests.get(url)



data=r.json()
df=pd.DataFrame(data)

# CSV 파일로 저장
df.to_csv("data.csv", index=False)

# 엑셀 파일로 저장
df.to_excel("data.xlsx", index=False)


print(df)
