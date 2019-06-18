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
    p_countrycode=req.form['p_countrycode']
    csv.register_dialect(
        'mydialect',
        delimiter=',',
        quotechar='"',
        doublequote=True,
        skipinitialspace=True,
        lineterminator='\r\n',
        quoting=csv.QUOTE_MINIMAL)

    url = "http://www.kamis.or.kr/service/price/xml.do?action=periodProductList&p_productclscode=01&p_startday=2015-10-01&p_endday=2015-12-01&p_itemcategorycode=200&p_itemcode=211&p_cert_key=9f1eafec-6bfe-4b7f-a0e0-0de934a470f9&p_cert_id=bitcocom1&p_returntype=json&p_countrycode="+p_countrycode
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
                    indict = {}
                    if element['countyname']=="평균" :
                        data=element['yyyy']+""+(element['regday'].replace('/',''))
                        indict['yyyy']=data
                        indict['price'] = element['price'].replace(',','')
                        datePrice.append(indict)

                with open('price'+p_countrycode+'.csv', 'w', newline='') as mycsvfile:
                    thedatawriter = csv.writer(mycsvfile, dialect='mydialect')
                    for row in datePrice:
                        d=[]
                        d.append(row['yyyy'])
                        d.append(int(row['price']))
                        thedatawriter.writerow(d)

                return json.dumps(datePrice)
        else:
            print("Error Code:" + rescode)
    except:
        print("Exception Code:" + rescode)

@app.route("/gostn_id", methods=['POST'])
def get_datestn_id():
    stnIds=req.form['stn_id']
    csv.register_dialect(
        'mydialect',
        delimiter=',',
        quotechar='"',
        doublequote=True,
        skipinitialspace=True,
        lineterminator='\r\n',
        quoting=csv.QUOTE_MINIMAL)

    url = "http://data.kma.go.kr/apiData/getData?type=json&dataCd=ASOS&dateCd=DAY&startDt=20151001&endDt=20151201&schListCnt=100&pageIndex=1&apiKey=oHsSmyZgv6U6120Oq257pCWnaK374OimRkgXiKzYoQ0Xxtqcfs3rw5O6iQOE9Rpt&stnIds="+stnIds
    request = urllib.request.Request(url)
    try:
        response = urllib.request.urlopen(request)
        rescode = response.getcode()
        if (rescode == 200):
            response_body = response.read()
            result = response_body.decode('utf-8')
            js = json.loads(result)
            if js:
                weather=js[3]['info']
                dataList=[]
                for data in weather :
                    dict_list = dict()
                    TM = data['TM'].replace('-','')
                    AVG_TA = data['AVG_TA']
                    MIN_TA = data['MIN_TA']
                    MAX_TA = data['MAX_TA']
                    SUM_RN = data.get('SUM_RN', 0)
                    dict_list['TM']=TM
                    dict_list['AVG_TA'] = AVG_TA
                    dict_list['MIN_TA'] = MIN_TA
                    dict_list['MAX_TA'] = MAX_TA
                    dict_list['SUM_RN'] = SUM_RN
                    dataList.append(dict_list)

                with open('weather'+stnIds+'.csv', 'w', newline='') as mycsvfile:
                    thedatawriter = csv.writer(mycsvfile, dialect='mydialect')
                    for row in dataList:
                        d=[]
                        d.append(row['TM'])
                        d.append(row['AVG_TA'])
                        d.append(row['MIN_TA'])
                        d.append(row['MAX_TA'])
                        d.append(row['SUM_RN'])
                        thedatawriter.writerow(d)

                return json.dumps(dataList)
        else:
            print("Error Code:" + rescode)
    except:
        print("Exception Code:" + rescode)
'''
@app.route("/merge", methods=['get'])
def dataMerge() :
    i=0
    while i<len(datePrice) :
        
        dataList['price']=datePrice[i]['price']
'''
if __name__ == '__main__':
    app.run(debug=True)