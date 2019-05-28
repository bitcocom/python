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

# 실습 4 : 결측지 보기
# print(shop_2018_01.isnull().sum())
#
# rc('font', family='HYKANM',size=50)
# dtf = msno.matrix(shop_2018_01)
# dtf.plot()
# plt.savefig('missing.png', dpi=100)
# plt.show ()

# 실습 5 : plotnine의 ggplot() 함수를 이용하여 위도, 경도 시각화(서울, 부산)
# print(ggplot(shop_2018_01[:1000])
# + aes(x='경도',y='위도')
# + geom_point(alpha=0.2, size=0.2)
# + theme(text=element_text(family='HYKANM'))
#   )

# 실습 6 : 서울 정보만 가지고 시각화
# shop_seoul = shop_2018_01.loc[shop_2018_01['도로명주소'].str.startswith('서울')]
# shop_except_seoul = shop_2018_01.loc[~shop_2018_01['도로명주소'].str.startswith('서울')]
# print(shop_seoul.shape)
# print(shop_except_seoul.shape)
#
# print(ggplot(shop_seoul)
#  + aes(x='경도',y='위도')
#  + geom_point(color='black', alpha=0.2, size=0.2)
#  + theme(text=element_text(family='HYKANM'))
# )

# 실습 7 : 도로명 주소에서 시도와 구군을 추가하기
# shop_2018_01['시도']=shop_2018_01['도로명주소'].str.split(' ', expand=True)[0]
# shop_2018_01['구군']=shop_2018_01['도로명주소'].str.split(' ', expand=True)[1]
# print(shop_2018_01.shape)
# print(shop_2018_01.columns)

# 실습 8 : 서울 지역만 구군으로 시각화 하기
shop_2018_01['시도']=shop_2018_01['도로명주소'].str.split(' ', expand=True)[0]
shop_2018_01['구군']=shop_2018_01['도로명주소'].str.split(' ', expand=True)[1]

shop_seoul = shop_2018_01.loc[shop_2018_01['도로명주소'].str.startswith('서울')]
print(ggplot(shop_seoul)
 + aes(x='경도',y='위도', color='구군')
 + geom_point(alpha=0.2, size=0.2)
 + theme(text=element_text(family='HYKANM'))
 + scale_fill_gradient(low='blue', high='green'))
