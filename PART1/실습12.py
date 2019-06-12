import os
import sys
import urllib.request
import json
# 배추가격 정보 가져오기
url="http://www.kamis.or.kr/service/price/xml.do?action=periodProductList&p_productclscode=01&p_startday=2015-10-01&p_endday=2015-12-01&p_itemcategorycode=200&p_itemcode=211&p_cert_key=9f1eafec-6bfe-4b7f-a0e0-0de934a470f9&p_cert_id=bitcocom1&p_returntype=json"

def get_datePrice():
    request = urllib.request.Request(url)
    try:
        response = urllib.request.urlopen(request)
        rescode = response.getcode()
        if (rescode == 200):
            response_body = response.read()
            result = response_body.decode('utf-8')
            js = json.loads(result)
            if js:
                datePrice = []
                point = js["data"]
                for element in point["item"]:
                    if element['countyname']=="평균" :
                        data=element['yyyy']+"/"+(element['regday'])
                        datePrice.append((data, element['price']))
                return datePrice
        else:
            print("Error Code:" + rescode)
    except:
        print("Exception Code:" + rescode)

data=get_datePrice()
for f in data :
    print(f)