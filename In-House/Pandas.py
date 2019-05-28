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
#print(shop_2018_01.shape)
#print(shop_2018_01.head(3))
#print(shop_2018_01.tail(3))
# print(shop_2018_01.columns)
# view_columns=['상호명','지점명','상권업종대분류명',
#                   '상권업종중분류명','상권업종소분류명',
#                   '시도명','시군구명','행정동명','법정동명','지번주소','경도', '위도']
# print(shop_2018_01[view_columns].head())
#print(shop_2018_01.isnull().sum())
#
#shop_2018_01['시도']=shop_2018_01['도로명주소'].str.split(' ', expand=True)[0]
#shop_2018_01['구군']=shop_2018_01['도로명주소'].str.split(' ', expand=True)[1]
shop_seoul = shop_2018_01.loc[shop_2018_01['도로명주소'].str.startswith('서울')]
# shop_except_seoul = shop_2018_01.loc[~shop_2018_01['도로명주소'].str.startswith('서울')]
# print(shop_seoul.shape)
# print(shop_except_seoul.shape)
#
# print(ggplot(shop_seoul)
# + aes(x='경도',y='위도')
# + geom_point(alpha=0.2, size=0.2)
# + theme(text=element_text(family='HYKANM'))
#       )
# print(ggplot(shop_seoul)
# + aes(x='경도',y='위도', color='구군')
# + geom_point(alpha=0.2, size=0.2)
# + theme(text=element_text(family='HYKANM'))
# + scale_fill_gradient(low='blue', high='green'))
#
shop_seoul = shop_2018_01.loc[shop_2018_01['도로명주소'].str.startswith('서울')]
shop_seoul_edu=shop_seoul.loc[shop_seoul['상권업종중분류명']=='학원-컴퓨터']
def show_marker_map(geo_df) :
     map = folium.Map(location=[geo_df['위도'].mean(),geo_df['경도'].mean()],
                      zoom_start=12, tiles='Stamen Terrain')
     for n in geo_df.index :
         shop_name = geo_df.loc[n,'상호명']+'-'+geo_df.loc[n,'도로명주소']
         folium.Marker([geo_df.loc[n,'위도'],geo_df.loc[n,'경도']], popup=shop_name).add_to(map)

     return map

map=show_marker_map(shop_seoul_edu)
svFilename = 'map.html'
map.save(svFilename)
webbrowser.open(svFilename)
#
# import missingno as msno
# import matplotlib.pyplot as plt
#
#  dtf=msno.matrix(shop_2018_01)
#  dtf.plot()
#  plt.savefig('output.png')

#rc('font', family='HYKANM',size=50)
#dtf = msno.matrix(shop_2018_01)
#dtf.plot()
#plt.savefig('missing.png', dpi=100)
#plt.show ()

# fig1 = plt.gcf()
# plt.show()
# plt.draw()
# fig1.savefig('tessstttyyy.png', dpi=100)