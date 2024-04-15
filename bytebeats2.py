#!/usr/bin/python3
# bytebeats0.py
import math
import pyaudio
import pydub

PyAudio = pyaudio.PyAudio
pa = PyAudio()
audio = pa.open(format=pa.get_format_from_width(1),channels=1,rate=8000,output=True)

samp=8000
freq=220
f = 8000/freq
t=0
while True:
    data = chr(int(
               ((math.sin((t/f*((t>>7)%13))*2*math.pi))/2)*127+128
              ) % 256)
    sound = pydub.AudioSegment(bytes(data, 'utf-8'), sample_width=1, channels=1, frame_rate=8000)
    quieter = sound + 5
    audio.write(quieter.raw_data)
    t += 1
