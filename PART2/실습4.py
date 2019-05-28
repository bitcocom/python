# 파이썬을 활용한 공공데이터 매장 위치 분석하기
# https://www.data.go.kr 홈페이지에서 상권정보 파일을 다운 받는다
import warnings
warnings.filterwarnings('ignore')
import pandas as pd
import missingno as msno
from plotnine import *
import matplotlib.pyplot as plt
from matplotlib import rc

# pandas : 구조화된 데이터의 처리를 지원하는 Python 라이브러리(파이썬계 엑셀이다)
# 실습 0 : cvs 파일 정보 불러오기
shop_2018_01=pd.read_csv('data/shop_201806/shop_201806_01.csv',encoding='cp949')

# 실습 1 : 파일 개수 출력하기
print(shop_2018_01.shape)

# 실습 2 : 처음 3개, 마지막 3개씩만 가져오기
print(shop_2018_01.head(3))
print(shop_2018_01.tail(3))

# 실습 3 : 컬럼명가져오기 , 원한는 컬럼가져오기
print(shop_2018_01.columns)
view_columns=['상호명','지점명','상권업종대분류명',
                   '상권업종중분류명','상권업종소분류명',
                   '시도명','시군구명','행정동명','법정동명','지번주소','경도', '위도']
print(shop_2018_01[view_columns].head())
