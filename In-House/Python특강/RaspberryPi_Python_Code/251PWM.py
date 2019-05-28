# DGPIO PWM Test
# Jonathan Suh www.creapple.com

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
LED = 12
GPIO.setup(LED, GPIO.OUT)

GPIO_PWM = GPIO.PWM(LED, 100)
GPIO_PWM.start(0)

try:
    while True:
        for i in range(0, 100):
            GPIO_PWM.ChangeDutyCycle(i)
            time.sleep(0.1)
        
except KeyboardInterrupt:
    GPIO_PWM.stop()
    GPIO.cleanup()
    
