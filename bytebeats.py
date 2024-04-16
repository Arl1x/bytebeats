#!/usr/bin/python3
import math
import utils


sample_width = 1
channels = 1
rate = 8000
output = True
freq = 220
f = rate / freq
t = 0
audio = utils.create_PyAudio(sample_width, channels, rate, output)

while True:
    expr = t | t * 4 | t * 12 | t * 36 | t * 2
    data = utils.create_sound_data(expr)
    sound = utils.create_AudioSegment(data, sample_width, channels, rate)
    quieter_sound = utils.lower_volume(sound, 6)
    audio.write(quieter_sound.raw_data)
    t += 1
