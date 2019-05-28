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

shop_seoul_edu=shop_seoul.loc[shop_seoul['상권업종중분류명']=='학원-컴퓨터']

# 실습12 : 학원-컴퓨터 상권을 지도로 시각화 하기
def show_marker_map(geo_df):
    map = folium.Map(location=[geo_df['위도'].mean(), geo_df['경도'].mean()],
                     zoom_start=12, tiles='Stamen Terrain')
    for n in geo_df.index:
        shop_name = geo_df.loc[n, '상호명'] + '-' + geo_df.loc[n, '도로명주소']
        folium.Marker([geo_df.loc[n, '위도'], geo_df.loc[n, '경도']], popup=shop_name).add_to(map)

    return map

map = show_marker_map(shop_seoul_edu)
svFilename = 'map.html'
map.save(svFilename)
webbrowser.open(svFilename)