import RPi.GPIO as GPIO
import time
import cv2
import datetime
import proj

num = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_russian_plate_number.xml')

ir = 8
green_led = 38
red_led = 40
n = 0

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.cleanup()

GPIO.setup(ir, GPIO.IN)
GPIO.setup(green_led, GPIO.OUT)
GPIO.setup(red_led, GPIO.OUT)

while True:

    GPIO.output(green_led, GPIO.HIGH)
    GPIO.output(red_led, GPIO.LOW)
    
    time.sleep(10)

    GPIO.output(green_led, GPIO.LOW)
    GPIO.output(red_led, GPIO.HIGH)

    start = time.time()

    while True:

        val = GPIO.input(ir)
        
        if val == 1:
            n += 1
            
            image = proj.detect()
            
            cv2.imwrite(str(n) + ".jpg", image)

        if (time.time() - start) > 10:
            break
