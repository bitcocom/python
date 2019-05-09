"""
파이썬 : MASH UP Service

편의시설 알리미

"""
import os
import sys
import urllib.request
import json
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# 서울열린데이터광장 data.seoul.go.kr에서 지하철역정보를 사용하기 위해 등록한 인증키  
seoul_id = "7443496561626974353343667a6843"
# 네이버 오픈 API에서 지하철역정보를 사용하기 위해 등록한 인증키 
naver_id = "4ibvf7a7s4"  # 네이버 인증 Client_id
naver_secret = "pcfd4vM5IVLhIpr1dgfWZyqVDIQZoCD6o3tCkQwx"  # 네이버 인증 Secret
naver_url = "file://kepco/python"  # 비로그인 오픈 API를 사용하기 위해 등록한 웹 서비스 URL
crs_code = "NHN:128"  # 서울열린데이터광장 지하철역정보에서 제공하는 좌표표준
# Mash up서비스를 위한 오픈 API URL 
URL_STATION = "http://openapi.seoul.go.kr:8088/"  # 서울열린데이터광장 지하철역정보
URL_LOCAL = "https://openapi.naver.com/v1/search/local?query="  # 네이버 주변지역 정보
URL_STATICMAP = "https://naveropenapi.apigw.ntruss.com/map-static/v2/raster?"  # 네이버 지도 API


# x, y좌표를 이용하여 지도를 표시
def map_service(point_x, point_y):
    if point_x == 0 and point_y == 0:
        lbl_Image.configure(text="주소를 확인할 수 없습니다.")
    else:
        url = URL_STATICMAP
        url += "crs=" + crs_code
        url += "&center=" + str(point_x) + "," + str(point_y)
        url += "&level=16&w=700&h=250"
        url += "&markers=type:d|size:mid|pos:"+ str(point_x) +'+'+ str(point_y)
        print(url)
        # URL_STATICMAP+"crs=NHN:128&w=300&h=300&markers=type:d|size:tiny|pos:"+316044%20575079"

        request = urllib.request.Request(url)
        request.add_header("X-NCP-APIGW-API-KEY-ID", naver_id)
        request.add_header("X-NCP-APIGW-API-KEY", naver_secret)
        try:
            response = urllib.request.urlopen(request)
            rescode = response.getcode()
            if (rescode == 200):
                photo = PhotoImage(format='png', data=response.read())
                lbl_Image.configure(image=photo)
                f = open("map.png", "wb")
                lbl_Image.photo = photo
            else:
                print("Error Code:" + rescode)
        except:
            print("Exception Code:" + rescode)


# 노선번호를 표시하는 comboLine를 변경할 경우 해당노선의 역정보를 가져옴
def change_comboLine(*args):
    line = comboLine.get()
    set_stations(line)


# 프로그램을 실행하면 초기값인 1호선, 노선번호를 표시하는 comboLine를 변경할 경우 해당 호선의 역정보를 가져옴
def set_stations(line):
    lineNumber = line[:1]
    url = URL_STATION + seoul_id
    url += "/json/SearchSTNBySubwayLineService/1/100/" + lineNumber
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
                point = js["SearchSTNBySubwayLineService"]
                # data = json.loads(point)
                for element in point["row"]:
                    # 가져온 역명에 "역"을 붙여줌
                    station.append(element["STATION_NM"] + "역")
                # 가져온 역명 Station Array를 역을 표시하는 comboStation에 assign하고 첫 값을 표시함
                comboStation['values'] = station
                comboStation.current(0)

        else:
            print("Error Code:" + rescode)
    except:
        print("Exception Code:" + rescode)


# 선택한 역과 검색어를 합해서 주변의 편의시설을 찾아줌
def search_place():
    # 선택한 역과 검색어
    place = strStation.get() + strEntry.get()
    encText = urllib.parse.quote(place)
    url = URL_LOCAL + encText
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", "mJJNeEVkJsiUdn3JDOjA")
    request.add_header("X-Naver-Client-Secret", "VRjWYSZMnO")
    try:
        response = urllib.request.urlopen(request)
        rescode = response.getcode()
        if (rescode == 200):
            response_body = response.read()
            result = response_body.decode('utf-8')
            js = json.loads(result)
            if js:
                # 기존에 treePlace에 장소정보를 가져온 것이 있으면 모두 지워줌
                treePlace.delete(*treePlace.get_children())
                # 새로 가져온 장소정보를 treePlace에 표시함
                for element in js["items"]:
                    treePlace.insert("", 'end', iid=None, text=element["title"],
                                     values=[element["category"], element["telephone"], element["address"],
                                             element["description"], element["mapx"], element["mapy"]])

        else:
            print("Error Code:" + rescode)
    except:
        print("Exception Code:" + rescode)


# treePlace에 표시된 주변의 편의시설 중 선택하면 상세정보를 보여줌
def place_selected(event):
    for item in treePlace.selection():
        item_text = treePlace.item(item, "values")
        lbl_Address.configure(text=item_text[2])
        lbl_Description.configure(text=item_text[3])
        # 가져온 좌표정보를 이용하여 지도에 표시함
        map_service(item_text[4], item_text[5])


# 화면에 tkinter UI componets를 배치함
window = Tk()
window.title("Mash up 편의시설 알리미")
window.geometry("800x800")
window.resizable(0, 0)

lbl_title = Label(window, text="편의시설 알리미", font=("돋움체", 20))
lbl_title.pack(padx=5, pady=15)
# 조회하기 위한 Header를 표시
labelLine = Label(window, text="노선번호")
labelLine.place(x=50, y=70, width=120, height=25)
labelStation = Label(window, text="역이름")
labelStation.place(x=250, y=70, width=120, height=25)
labelEntry = Label(window, text="편의시설")
labelEntry.place(x=500, y=70, width=120, height=25)

# 노선정보를 선택하기 위한 Combobox
strLine = StringVar()
comboLine = ttk.Combobox(window, width=20, textvariable=strLine)
comboLine['values'] = ('1호선', '2호선', '3호선', '4호선', '5호선', '6호선', '7호선', '8호선')
comboLine.place(x=50, y=100, width=120, height=25)
comboLine.current(0)
# 노선정보를 선택하면 change_comboLine을 실행함
comboLine.bind("<<ComboboxSelected>>", change_comboLine)

# 해당 노선의 역정보를 선택하기 위한 Combobox
strStation = StringVar()
comboStation = ttk.Combobox(window, width=20, textvariable=strStation)
comboStation.place(x=200, y=100, width=230, height=25)
# 초기값은 맨 위에있는 1호선의 역사를 표시함
set_stations(strLine.get())

# 주변시설 검색어를 넣는 Entry (Option value)
strEntry = StringVar()
entrySearch = Entry(window, width=20, textvariable=strEntry, font=("돋움체", 14))
entrySearch.place(x=460, y=100, width=200, height=25)

# 검색을 실행하는 Button
btn_action = Button(window, text="검색", command=search_place, font=("돋움체", 14))
btn_action.place(x=700, y=100, width=50, height=25)

# 검색한 주변시설을 표시하는 treePlace
treePlace = ttk.Treeview(window)
treePlace["columns"] = ("category", "telephone")
treePlace.column("category", width=100)
treePlace.column("telephone", width=100)
# treePlace에는 명칭, 분류, 전화번호만 표시함
treePlace.heading("#0", text="명칭")
treePlace.heading("category", text="분류")
treePlace.heading("telephone", text="전화번호")
treePlace.place(x=50, y=150, width=700, height=300)
# 검색한 주변시설 중 하나를 선택하면 place_selected을 실행함 
treePlace.bind("<<TreeviewSelect>>", place_selected)

# 검색한 주변시설 중 하나를 선택하면 주소와 설명을 표시함
labelAddress = Label(window, text="주소")
labelAddress.place(x=50, y=460, width=50, height=25)
labelDescription = Label(window, text="설명")
labelDescription.place(x=50, y=490, width=50, height=25)
lbl_Address = Label(window, text="", font=("돋움체", 12), anchor="w")
lbl_Address.place(x=100, y=460, width=600, height=25)
lbl_Description = Label(window, text="", font=("돋움체", 12), anchor="w")
lbl_Description.place(x=100, y=490, width=600, height=25)
# 검색한 주변시설 중 하나를 선택하면 지도로 표시함
lbl_Image = Label(window, image=None, text="", font=("돋움체", 20))
lbl_Image.place(x=50, y=530, width=700, height=250)

window.mainloop()

