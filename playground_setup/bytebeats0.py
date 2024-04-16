#!/usr/bin/python3
# bytebeats0.py
import math

samp=8000
freq=220
f = 8000/freq
t=0
while True:
    print(chr(int(
        ((math.sin((t/f*((t>>7)%13))*2*math.pi))/2)*127+128
        ) % 256), end='')
    t += 1
