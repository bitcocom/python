from bs4 import BeautifulSoup
import urllib.request as req
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = "https://sum.su.or.kr:8888/bible/today"
res = req.urlopen(url).read()
soup = BeautifulSoup(res, "html.parser")

# 따라하기
dailybible_info = str(soup.select_one("#dailybible_info").string)
print("{0}".format(dailybible_info.strip()))

bible_text = str(soup.select_one("#bible_text").string)
print("{0}".format(bible_text.strip()))

bibleinfo_box = str(soup.select_one("#bibleinfo_box").string)
print("{0}".format(bibleinfo_box.strip()))

num_info = soup.select(".body_list > li")
for e in num_info:
         print(e.select_one(".num").string,":",e.select_one(".info").string)

