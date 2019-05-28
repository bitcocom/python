# Remote Car Control with Video Streaming by Flask web service    
# Jonathan Suh www.creapple.com

#Import GPIO, time library
from flask import Flask, render_template, request, Response
import RPi.GPIO as GPIO                 
import time      
import io
import threading
import picamera

class Camera:
    thread = None  # background thread that reads frames from camera
    frame = None  # current frame is stored here by background thread
    start_time = 0  # time of last client access to the camera

    def getStreaming(self):
        Camera.start_time = time.time()
        #self.initialize()
        if Camera.thread is None:
            # start background frame thread
            Camera.thread = threading.Thread(target=self.streaming)
            Camera.thread.start()

            # wait until frames start to be available
            while self.frame is None:
                time.sleep(0)
        return self.frame

    @classmethod
    def streaming(c):
        with picamera.PiCamera() as camera:
            # camera setup
            camera.resolution = (320, 240)
            camera.hflip = True
            camera.vflip = True

            # let camera warm up
            camera.start_preview()
            time.sleep(2)

            stream = io.BytesIO()
            for f in camera.capture_continuous(stream, 'jpeg',
                                                 use_video_port=True):
                # store frame
                stream.seek(0)
                c.frame = stream.read()

                # reset stream for next frame
                stream.seek(0)
                stream.truncate()

                # if there hasn't been any clients asking for frames in
                # the last 10 seconds stop the thread
                if time.time() - c.start_time > 10:
                    break
        c.thread = None
        
app = Flask(__name__)

#Set GPIO BCM(Broadcom SoC) pin number 
GPIO.setmode(GPIO.BCM)      

TRIG = 23                                  
ECHO = 24                                  

GPIO.setup(TRIG,GPIO.OUT)                  
GPIO.setup(ECHO,GPIO.IN)

RIGHT_FORWARD = 26                                  
RIGHT_BACKWARD = 19                                   
RIGHT_PWM = 13
LEFT_FORWARD = 21                                  
LEFT_BACKWARD = 20                                   
LEFT_PWM = 16 

GPIO.setup(RIGHT_FORWARD,GPIO.OUT)                  
GPIO.setup(RIGHT_BACKWARD,GPIO.OUT)
GPIO.setup(RIGHT_PWM,GPIO.OUT)
GPIO.output(RIGHT_PWM, 0)
RIGHT_MOTOR = GPIO.PWM(RIGHT_PWM, 100)
RIGHT_MOTOR.start(0)
RIGHT_MOTOR.ChangeDutyCycle(0)

GPIO.setup(LEFT_FORWARD,GPIO.OUT)                  
GPIO.setup(LEFT_BACKWARD,GPIO.OUT)
GPIO.setup(LEFT_PWM,GPIO.OUT)
GPIO.output(LEFT_PWM, 0)
LEFT_MOTOR = GPIO.PWM(LEFT_PWM, 100)
LEFT_MOTOR.start(0)
LEFT_MOTOR.ChangeDutyCycle(0)

#Get distance from HC-SR04 
def getDistance():
  GPIO.output(TRIG, GPIO.LOW)                 
  time.sleep(1)                            

  GPIO.output(TRIG, GPIO.HIGH)                  
  time.sleep(0.00001)                      
  GPIO.output(TRIG, GPIO.LOW)

  #When the ECHO is LOW, get the purse start time
  while GPIO.input(ECHO)==0:                
    pulse_start = time.time()               
  
  #When the ECHO is HIGN, get the purse end time
  while GPIO.input(ECHO)==1:               
    pulse_end = time.time()                 

  #Get pulse duration time
  pulse_duration = pulse_end - pulse_start 
  #Multiply pulse duration by 17150 to get distance and round
  distance = pulse_duration * 17150        
  distance = round(distance, 2)           
 
  return distance

#Right Motor Control 
def rightMotor(forward, backward, pwm):
  GPIO.output(RIGHT_FORWARD,forward)
  GPIO.output(RIGHT_BACKWARD,backward)
  RIGHT_MOTOR.ChangeDutyCycle(pwm)

#Left Motor Control 
def leftMotor(forward, backward, pwm):
  GPIO.output(LEFT_FORWARD,forward)
  GPIO.output(LEFT_BACKWARD,backward)
  LEFT_MOTOR.ChangeDutyCycle(pwm)

#Forward Car
def forward():
    rightMotor(1, 0, 70)
    leftMotor(1, 0, 70)
    time.sleep(1)

#Left Car
def left():
    rightMotor(0, 0, 0)
    leftMotor(1, 0, 70)
    time.sleep(0.3)

#Right Car
def right():
    rightMotor(1, 0, 70)
    leftMotor(0, 0, 0)
    time.sleep(0.3)

#Stop Car
def stop():
    rightMotor(0, 0, 0)
    leftMotor(0, 0, 0)

@app.route("/<command>")
def action(command):
    distance_value = getDistance()
    if command == "F":
        forward()
        message = "Moving Foward"
    elif command == "L":
        left() 
        message = "Turn Left"
    elif command == "R":
        right()   
        message = "Turn Right"  
    else:
        stop()
        message = "Unknown Command [" + command + "] " 

    msg = {
        'message' : message,
        'distance': str(distance_value)
    }
        
    return render_template('video.html', **msg)

def show(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.getStreaming()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/show')
def showVideo():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(show(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    try:
        app.run(host='0.0.0.0', port=8300, debug=True, threaded=True)
    except KeyboardInterrupt:
        print ("Terminate program by Keyboard Interrupt")
        GPIO.cleanup()
