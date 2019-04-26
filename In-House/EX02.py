# AEX02
class Ball:
    color = ""
    speed = 0
    #생성자 함수(초기화)
    def __init__(self, color=None, speed=None):
        self.color=color
        self.speed=speed

    def setSpeed(self, value):
        self.speed = value

#객체생성
ball01 = Ball()
ball01.color="Blue"
ball01.setSpeed(30)
print(ball01.color, ball01.speed)

ball02 = Ball("Red", 50) #객체생성 후 초기화
print(ball02.color, ball02.speed)
