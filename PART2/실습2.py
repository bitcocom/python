# 실습 2 : 한국전력 홈페이지에서 공지사항 가져오기
'''
     http://home.kepco.co.kr/kepco/main.do
'''
from bs4 import BeautifulSoup
import urllib.request as req
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = "http://home.kepco.co.kr/kepco/main.do"
res = req.urlopen(url).read()
soup = BeautifulSoup(res, "html.parser")

# 실습 2 : 아래에 코드를 작성하시오.( 3곳에 채워 넣으시면 됩니다.)
num_info = soup.select(                )
for e in num_info:
         print(e.select_one(          ).string,":",e.select_one(        ).string)