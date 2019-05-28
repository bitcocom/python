import warnings
warnings.filterwarnings('ignore')
import pandas as pd
import missingno as msno
from plotnine import *
import matplotlib.pyplot as plt
from matplotlib import rc
import folium
import webbrowser

shop_2018_01=pd.read_csv('data/shop_201806/shop_201806_01.csv',encoding='cp949')

shop_2018_01['시도']=shop_2018_01['도로명주소'].str.split(' ', expand=True)[0]
shop_2018_01['구군']=shop_2018_01['도로명주소'].str.split(' ', expand=True)[1]

shop_seoul = shop_2018_01.loc[shop_2018_01['도로명주소'].str.startswith('서울')]

# 실습 9 : 상권업종대분류명 기준으로 데이터 시각화 하기
# print(shop_seoul['상권업종대분류명'].value_counts())
# print(ggplot(shop_seoul)
#  + aes(x='경도',y='위도', color='상권업종대분류명')
#  + geom_point(alpha=0.2, size=0.2)
#  + theme(text=element_text(family='HYKANM'))
#  + scale_fill_gradient(low='blue', high='green'))

# 실습 10 : 상권업종대분류명이 == '학문/교육' 인경우만 시각화 하기
# shop_seoul_edu=shop_seoul.loc[shop_seoul['상권업종대분류명']=='학문/교육']
# print(ggplot(shop_seoul_edu)
#  + aes(x='경도',y='위도', color='상권업종중분류명')
#  + geom_point(alpha=0.2, size=0.2)
#  + theme(text=element_text(family='HYKANM'))
#  + scale_fill_gradient(low='blue', high='green'))

# 실습 11 : 상권업종중분류명이 == '학원-컴퓨터' 인경우만 시각화 하기
shop_seoul_edu=shop_seoul.loc[shop_seoul['상권업종중분류명']=='학원-컴퓨터']
print(ggplot(shop_seoul_edu)
 + aes(x='경도',y='위도', color='상권업종중분류명')
 + geom_point(alpha=0.2, size=0.2)
 + theme(text=element_text(family='HYKANM'))
 + scale_fill_gradient(low='blue', high='green'))
