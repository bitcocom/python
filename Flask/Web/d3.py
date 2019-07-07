import json
import flask
import numpy as np

app = flask.Flask(__name__)


# d3sample 을 호출했을때의 템플릿 설정
@app.route("/d3sample")
def showsample():
    return flask.render_template("d3.html")


# D3에서 가져갈 data url을 호출하면 반환할 json 데이터 만들어 내기
@app.route("/data")
def data():
    # 데이터 지정
    x = np.array(['2017-07-10', '2017-07-11', '2017-07-12', '2017-07-13', '2017-07-14'])
    y = np.array([58.13, 53.98, 67.00, 89.70, 99.00])

    # 리스트를 json 데이터로 변환
    return json.dumps([{"date": x[i], "close": y[i]}
                       for i in range(5)])


# 앞과 비슷한데 조금 틀려만 보임
if __name__ == "__main__":
    port = 5000
    app.debug = True
    app.run(port=port)
