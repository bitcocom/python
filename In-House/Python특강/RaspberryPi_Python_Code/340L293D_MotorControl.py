# Control 2 DC Motor using L293D   
# Jonathan Suh www.creapple.com

#Import GPIO, time library
import RPi.GPIO as GPIO                    
import time                                

#Set GPIO BCM(Broadcom SoC) pin number 
GPIO.setmode(GPIO.BCM)                     

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
      #Forward 5 seconds
      rightMotor(1, 0, 70)
      leftMotor(1, 0, 70)
      time.sleep(5)

      #Right 5 seconds
      rightMotor(1, 0, 70)
      leftMotor(0, 0, 0)
      time.sleep(5)

      #Left 5 seconds
      rightMotor(0, 0, 0)
      leftMotor(1, 0, 70)
      time.sleep(5)

      #Stop 5 seconds
      rightMotor(0, 0, 0)
      leftMotor(0, 0, 0)
      time.sleep(5)
      
  except KeyboardInterrupt:
    print ("Terminate program by Keyboard Interrupt")
    GPIO.cleanup()


