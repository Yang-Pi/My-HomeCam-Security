import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(1, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)

while True:
    input_state = GPIO.input(1)
    if input_state == False:
        while True:
            GPIO.output(18,GPIO.HIGH)
            GPIO.output(24,GPIO.LOW)
            time.sleep(0.1)
            GPIO.output(18,GPIO.LOW)
            GPIO.output(24,GPIO.HIGH)
            time.sleep(0.1)
