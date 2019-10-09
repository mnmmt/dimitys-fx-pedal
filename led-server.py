#!/usr/bin/env python

import sys
import socket
from time import sleep
from threading import Thread

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

for g in [2, 3, 4]:
    GPIO.setup(g, GPIO.OUT, initial=GPIO.LOW)

LEDPIN = 27

GPIO.setup(LEDPIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address = ('localhost', 9999)
#print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

def switchwatch(sock):
    last = 0
    while True:
      sw = GPIO.input(LEDPIN)
      if sw != last:
        sock2.sendto("%d %d;\n" % (LEDPIN, sw), ("localhost", 9998))
        last = sw
      sleep(0.1)

def lights(sock):
    while True:
        data, address = sock.recvfrom(4096)
        #print data
        pin, state = data.split(" ")
        state = state.replace(";", "").replace("\n", "")
        #print pin, state, "GPIO.HIGH" if int(state) else "GPIO.LOW"
        GPIO.output(int(pin), GPIO.HIGH if int(state) else GPIO.LOW)

try:
    t = Thread(target=switchwatch, args=(sock,))
    t.daemon = True
    t.start()
    lights(sock)
except (KeyboardInterrupt, SystemExit):
    print("Exiting.")
    GPIO.cleanup()

