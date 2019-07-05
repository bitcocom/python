import urllib.request
from bs4 import BeautifulSoup
html=urllib.request.urlopen("http://cyber.kepco.co.kr/ckepco/mobile/customer_support/find_area.jsp?sch_area=3970|3850")

soupData=BeautifulSoup(html, 'html.parser')
soup=soupData.select_one("#area_list")

soupP=soup.findAll('p', attrs={'class':'title_p'})
soupD=soup.findAll('p', attrs={'class':'date'})
print(len(soupD))
print(soupD)
result=[]
i=0
while i<len(soupD) :
    title=soup.findAll('p', attrs={'class': 'title_p'})[i].string
    date = soup.findAll('p', attrs={'class': 'date'})[i].string
    print(title, date)
    result.append([title]+[date])
    i=i+1

print(result)

import pandas as pd
kepco_table=pd.DataFrame(result, columns=('part','addr'))
kepco_table.to_csv("kepco.csv", encoding='cp949', mode='w', index=True)
print('csv 파일 생성 완료')