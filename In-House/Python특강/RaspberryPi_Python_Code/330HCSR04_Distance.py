# Distance test with Ultrasonic Sensor HCSR04
# Jonathan Suh www.creapple.com

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

TRIG = 23                                  
ECHO = 24

GPIO.setup(TRIG,GPIO.OUT)                  
GPIO.setup(ECHO,GPIO.IN)

def getDistance():
  GPIO.output(TRIG, False)                 
  time.sleep(1)  

  GPIO.output(TRIG, True)                  
  time.sleep(0.00001)                      
  GPIO.output(TRIG, False)

  while GPIO.input(ECHO)==0:               #Check whether the ECHO is LOW
    pulse_start = time.time()              #Saves the last known time of LOW pulse

  while GPIO.input(ECHO)==1:               #Check whether the ECHO is HIGH
    pulse_end = time.time()                #Saves the last known time of HIGH pulse 

  pulse_duration = pulse_end - pulse_start #Get pulse duration to a variable

  distance = pulse_duration * 17150        #Multiply pulse duration by 17150 to get distance
  distance = round(distance, 2)            #Round to two decimal points

  return distance

if __name__ == '__main__':
  try:
    while True:
      distance_value = getDistance()
      if distance_value > 2 and distance_value < 400:      
          print ("Distnace is %.2f cm" %distance_value)  #Print distance with 0.5 cm calibration
      else:
          print ("Out Of Range")                         #display out of range 


  except KeyboardInterrupt:
    print ("Terminate program by Keyboard Interrupt")
    GPIO.cleanup()
