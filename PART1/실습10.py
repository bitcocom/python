# 딕셔녀리 자료형(dict) : { key : value } -> JSON
st = {"STATION_CD":"1916","STATION_NM":"소요산","LINE_NUM":"1","FR_CODE":"100"}
print(type(st))
print(st)

# 주어진 JSON 데이터(문자열)를 파이썬의 사전(dict) 자료형으로 변환하여 역이름을 출력하시오.
import json
jsonData = '{"STATION_CD":"1916","STATION_NM":"소요산","LINE_NUM":"1","FR_CODE":"100"}'
print(type(jsonData))
dicData=json.loads(jsonData)
print("{0}역".format(dicData['STATION_NM']))

# 실습 10 : 파일에 저장된 JSON데이터를 읽어서 역명만 별도의 리스트로 만들어 출력하시오.
f = open('station.txt', 'r' , encoding='utf-8')
jsonStr = f.read()
print(jsonStr)
js = json.loads(jsonStr)
if js:
      station = []
      point = js["SearchSTNBySubwayLineService"]
      # data = json.loads(point)
      for element in point["row"]:
      # 가져온 역명에 "역"을 붙여줌
          station.append(element["STATION_NM"] + "역")

print(station)

# 활용 방법
# http://openapi.seoul.go.kr:8088/7443496561626974353343667a6843/json/SearchSTNBySubwayLineService/1/100/1