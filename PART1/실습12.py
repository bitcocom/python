import os
import sys
import urllib.request
import json
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

url="http://www.kamis.or.kr/service/price/xml.do?action=periodProductList&p_productclscode=01&p_startday=2015-10-01&p_endday=2015-12-01&p_itemcategorycode=200&p_itemcode=211&p_cert_key=9f1eafec-6bfe-4b7f-a0e0-0de934a470f9&p_cert_id=bitcocom1&p_returntype=json"

def set_stations():
    request = urllib.request.Request(url)
    try:
        response = urllib.request.urlopen(request)
        rescode = response.getcode()
        if (rescode == 200):
            response_body = response.read()
            result = response_body.decode('utf-8')
            js = json.loads(result)
            if js:
                station = []
                point = js["data"]
                #point1= point["data"]
                # data = json.loads(point)
                for element in point["item"]:
                    # 가져온 역명에 "역"을 붙여줌
                    if element['countyname']=="평균" :
                        data=element['yyyy']+"/"+(element['regday'])
                        station.append((data, element['price']))
                # 가져온 역명 Station Array를 역을 표시하는 comboStation에 assign하고 첫 값을 표시함
                return station
        else:
            print("Error Code:" + rescode)
    except:
        print("Exception Code:" + rescode)

data=set_stations()
for f in data :
    print(f)