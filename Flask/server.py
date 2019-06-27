# -*- coding: utf-8 -*-
from flask import Flask, render_template
from flask import request as req
import json
import urllib.request
import csv

app = Flask(__name__)

dataList = []
datePrice = []

@app.route("/", methods=['GET', 'POST'])
def index():
    if req.method == 'GET':
        return render_template('index.html')

@app.route("/go", methods=['POST'])
def get_datePrice():
    datePrice.clear()
    p_countrycode=str(req.form['p_countrycode'])
    p_startday = str(req.form['date3'])
    p_endday = str(req.form['date4'])
    pageIndex = 1
    while pageIndex<=4:
      if pageIndex == 1 :
         url = "http://www.kamis.or.kr/service/price/xml.do?action=periodProductList&p_productclscode=01&p_startday="+p_startday+"&p_endday=2012-12-31&p_itemcategorycode=200&p_itemcode=211&p_cert_key=9f1eafec-6bfe-4b7f-a0e0-0de934a470f9&p_cert_id=bitcocom1&p_returntype=json&p_countrycode="+p_countrycode
      if pageIndex == 2:
         url = "http://www.kamis.or.kr/service/price/xml.do?action=periodProductList&p_productclscode=01&p_startday=2013-01-01&p_endday=2014-12-31&p_itemcategorycode=200&p_itemcode=211&p_cert_key=9f1eafec-6bfe-4b7f-a0e0-0de934a470f9&p_cert_id=bitcocom1&p_returntype=json&p_countrycode=" + p_countrycode
      if pageIndex == 3:
         url = "http://www.kamis.or.kr/service/price/xml.do?action=periodProductList&p_productclscode=01&p_startday=2015-01-01&p_endday=2016-12-31&p_itemcategorycode=200&p_itemcode=211&p_cert_key=9f1eafec-6bfe-4b7f-a0e0-0de934a470f9&p_cert_id=bitcocom1&p_returntype=json&p_countrycode=" + p_countrycode
      if pageIndex == 4:
         url = "http://www.kamis.or.kr/service/price/xml.do?action=periodProductList&p_productclscode=01&p_startday=2017-01-01&p_endday=" + p_endday + "&p_itemcategorycode=200&p_itemcode=211&p_cert_key=9f1eafec-6bfe-4b7f-a0e0-0de934a470f9&p_cert_id=bitcocom1&p_returntype=json&p_countrycode=" + p_countrycode

      print(url)
      request = urllib.request.Request(url)
      try:
          response = urllib.request.urlopen(request)
          rescode = response.getcode()
          if (rescode == 200):
              response_body = response.read()
              result = response_body.decode('utf-8')
              js = json.loads(result)
              if js:
                  #datePrice = []
                  point = js["data"]
                  for element in point["item"]:
                      indict = {}
                      if element['countyname']=="평균" :
                          data=element['yyyy']+""+(element['regday'].replace('/',''))
                          indict['yyyy']=data
                          indict['price'] = element['price'].replace(',','')
                          datePrice.append(indict)
                  pageIndex=pageIndex+1
                  #return json.dumps(datePrice)
          else:
              #return json.dumps(datePrice)
              print("Error Code:" + rescode)
      except:
          #return json.dumps(datePrice)
          print("Exception Code:" + rescode)

    return json.dumps(datePrice)

@app.route("/gostn_id", methods=['POST'])
def get_datestn_id():
    dataList.clear()
    stnIds=req.form['stn_id']
    startDt = req.form['date1'].replace('-','')
    endDt = req.form['date2'].replace('-','')
    pageIndex =1
    while True :
      url = "http://data.kma.go.kr/apiData/getData?type=json&dataCd=ASOS&dateCd=DAY&startDt="+startDt+"&endDt="+endDt+"&schListCnt=100&pageIndex="+str(pageIndex)+"&apiKey=oHsSmyZgv6U6120Oq257pCWnaK374OimRkgXiKzYoQ0Xxtqcfs3rw5O6iQOE9Rpt&stnIds="+stnIds
      request = urllib.request.Request(url)
      print(pageIndex)
      try:
          response = urllib.request.urlopen(request)
          rescode = response.getcode()
          if (rescode == 200):
              response_body = response.read()
              result = response_body.decode('utf-8')
              js = json.loads(result)
              if js:
                  weather=js[3]['info']
                  pageIndex = pageIndex + 1
                  if len(weather) == 0 : break
                  #dataList=[]
                  for data in weather :
                      print(data)
                      dict_list = dict()
                      TM = data['TM'].replace('-','')
                      STN_NM=data['STN_NM']
                      if TM=='20171012' and STN_NM=='서울':
                          AVG_TA = data['AVG_TA']
                          MIN_TA = data['MIN_TA']
                          MAX_TA = 21.7
                          SUM_RN = 20
                      elif TM=='20130930' and STN_NM=='대구':
                          AVG_TA = 20.3
                          MIN_TA = data['MIN_TA']
                          MAX_TA = 22.3
                          SUM_RN = data['SUM_RN']

                      elif TM == '20170729' and STN_NM == '대구':
                          AVG_TA = 28.2
                          MIN_TA = data['MIN_TA']
                          MAX_TA = data['MAX_TA']
                          SUM_RN = data['SUM_RN']
                      else :
                          AVG_TA = data['AVG_TA']
                          MIN_TA = data['MIN_TA']
                          MAX_TA = data['MAX_TA']
                          SUM_RN = data.get('SUM_RN', 0)
                      dict_list['yyyy']=TM
                      dict_list['AVG_TA'] = AVG_TA
                      dict_list['MIN_TA'] = MIN_TA
                      dict_list['MAX_TA'] = MAX_TA
                      dict_list['SUM_RN'] = SUM_RN
                      dataList.append(dict_list)

          else:
              return json.dumps(dataList)
              print("Error Code:" + rescode)
      except:
          return json.dumps(dataList)
          print("Exception Code:" + rescode)

    return json.dumps(dataList)

@app.route("/merge", methods=['POST'])
def dataMerge() :
    p_countrycode = req.form['p_countrycode']
    csv.register_dialect(
        'mydialect',
        delimiter=',',
        quotechar='"',
        doublequote=True,
        skipinitialspace=True,
        lineterminator='\r\n',
        quoting=csv.QUOTE_MINIMAL)

    tmp = []
    for row in dataList:
        price=0
        for row1 in datePrice:
            if  row['yyyy'] == row1['yyyy']:
                row['price']=row1['price']
                price=row1['price']
                break
            else :
                row['price']=0
        tmp.append(row)

    i=0
    while i<len(tmp) :
       if tmp[i]['price']==0 :
            tmp[i]['price']=tmp[i-1]['price']
       i=i+1

    with open('final' + p_countrycode + '.csv', 'w', newline='') as mycsvfile:
        thedatawriter = csv.writer(mycsvfile, dialect='mydialect')
        title=['year','avgTemp','minTemp','maxTemp','rainFall','avgPrice']
        thedatawriter.writerow(title)
        #year,avgTemp,minTemp,maxTemp,rainFall,avgPrice
        for row in tmp:
            d = []
            d.append(row['yyyy'])
            d.append(row['AVG_TA'])
            d.append(row['MIN_TA'])
            d.append(row['MAX_TA'])
            d.append(row['SUM_RN'])
            d.append(row['price'])
            thedatawriter.writerow(d)

    return json.dumps(tmp)

if __name__ == '__main__':
    app.run(debug=True)