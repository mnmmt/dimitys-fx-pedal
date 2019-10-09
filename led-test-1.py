#!/usr/bin/env python

from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

# GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.setup(2, GPIO.OUT, initial=GPIO.LOW)

counter = False
while True:
    counter = not counter
    GPIO.output(2, GPIO.HIGH if counter else GPIO.LOW)
    sleep(0.5)
