# https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode
# X-NCP-APIGW-API-KEY-ID
# X-NCP-APIGW-API-KEY
'''
{
    "status": "OK",
    "meta": {
        "totalCount": 1,
        "page": 1,
        "count": 1
    },
    "addresses": [
        {
        "roadAddress": "경상남도 거제시 연초면 효촌1길 10-1",
        "jibunAddress": "경상남도 거제시 연초면 연사리 93",
        "englishAddress": "10-1, Hyochon 1-gil, Yeoncho-myeon, Geoje-si, Gyeongsangnam-do, Republic of Korea",
        "addressElements": [
            {
            "types": ["SIDO"],
            "longName": "경상남도",
            "shortName": "경상남도",
            "code": ""
            },
            {
            "types": ["SIGUGUN"],
            "longName": "거제시",
            "shortName": "거제시",
            "code": ""
            },
            {
            "types": ["DONGMYUN"],
            "longName": "연초면",
            "shortName": "연초면",
            "code": ""
            },
            {
            "types": ["RI"],
            "longName": "연사리",
            "shortName": "연사리",
            "code": ""
            },
            {
            "types": ["ROAD_NAME"],
            "longName": "효촌1길",
            "shortName": "효촌1길",
            "code": ""
            },
            {
            "types": ["BUILDING_NUMBER"],
            "longName": "10-1",
            "shortName": "10-1",
            "code": ""
            },
            {
            "types": ["BUILDING_NAME"],
            "longName": "",
            "shortName": "",
            "code": ""
            },
            {
            "types": ["LAND_NUMBER"],
            "longName": "93",
            "shortName": "93",
            "code": ""
            },
            {
            "types": ["POSTAL_CODE"],
            "longName": "53209",
            "shortName": "53209",
            "code": ""
            }
        ],
        "x": "128.6521583",
        "y": "34.9070498",
        "distance": 0
        }
    ],
    "errorMessage": ""
}
'''
# 실습 9 : 자신의 주소를 입력하고 입력된 주소의 위도 경도를 구하여 지도에 포시하시오.

import os
import sys
import urllib.request
import datetime
import time
import json
from config import *
def get_request_url(url):
    req = urllib.request.Request(url)
    req.add_header("X-NCP-APIGW-API-KEY-ID", "4ibvf7a7s4")
    req.add_header("X-NCP-APIGW-API-KEY", "pcfd4vM5IVLhIpr1dgfWZyqVDIQZoCD6o3tCkQwx")
    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print("[%s] Url Request Success" % datetime.datetime.now())
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL : %s" % (datetime.datetime.now(), url))
        return None

# [CODE 1]
def getGeoData(address):
    base = "https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode"
    node = ""
    parameters = "?query=%s" % urllib.parse.quote(address)
    url = base + node + parameters

    retData = get_request_url(url)

    if (retData == None):
        return None
    else:
        return json.loads(retData)
y = 0.0
x = 0.0
address =''
import folium
import webbrowser

def main():
    addr = input("주소 입력:")
    jsonResult = getGeoData(addr)
    if 'addresses' in jsonResult.keys():
         point = jsonResult["addresses"]
         print(point)
         for item in point :
             print(item)
             print('주소:' , item['roadAddress'])
             address = item['roadAddress']
             print('위도: ', str(item['y']))
             y=item['y']
             print('경도: ', str(item['x']))
             x=item['x']

    map = folium.Map(location=[y, x],zoom_start=17)
    folium.Marker([y, x], popup=address).add_to(map)
    svFilename = 'myHouse.html'
    map.save(svFilename)
    webbrowser.open(svFilename)

if __name__ == '__main__':
    main()