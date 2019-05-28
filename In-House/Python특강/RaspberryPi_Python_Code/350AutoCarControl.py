# Auto Car Control 2 DC Motor and Ultrasonic Sensor 
# Jonathan Suh www.creapple.com

#Import GPIO, time library
import RPi.GPIO as GPIO                    
import time                                

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

if __name__ == '__main__':
  try:
    while True:
      distance_value = getDistance()
      #Check whether the distance is 50 cm
      if distance_value > 50:      
          #Forward 1 seconds
          print ("Forward " + str(distance_value))
          rightMotor(1, 0, 70)
          leftMotor(1, 0, 70)
          time.sleep(1)
      else:
          #Left 1 seconds
          print ("Left " + str(distance_value))
          rightMotor(0, 0, 0)
          leftMotor(1, 0, 70)
          time.sleep(1)
      
  except KeyboardInterrupt:
    print ("Terminate program by Keyboard Interrupt")
    GPIO.cleanup()

