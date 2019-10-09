#!/usr/bin/env python

import sys
import socket
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

for g in [2, 3, 4]:
    GPIO.setup(g, GPIO.OUT, initial=GPIO.LOW)

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address = ('localhost', 9999)
#print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

while True:
    data, address = sock.recvfrom(4096)
    #print data
    pin, state = data.split(" ")
    state = state.replace(";", "").replace("\n", "")
    #print pin, state, "GPIO.HIGH" if int(state) else "GPIO.LOW"
    GPIO.output(int(pin), GPIO.HIGH if int(state) else GPIO.LOW)
