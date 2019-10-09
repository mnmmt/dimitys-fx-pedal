#!/usr/bin/env python

import sys
import socket
from time import sleep
from threading import Thread

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

for g in [2, 3, 4]:
    GPIO.setup(g, GPIO.OUT, initial=GPIO.LOW)

GPIO.output(2, GPIO.HIGH)

GPIO.cleanup()

