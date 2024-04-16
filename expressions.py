import math

# 8000hz = 1 second of time
t = 0
f = 220 / 8000

# pacman sounds, thanks fish
expr = ((math.sin((t / f * ((t >> 7) % 13)) * 2 * math.pi)) / 2) * 127 + 128

"""
This section was provided by the following PDF:
https://github.com/TuesdayNightMachines/Bytebeats/blob/master/Bytebeats_Beginners_Guide_TTNM_v1-5.pdf
This describes how the math affects the waveforms that will be generated.
Frequency is the speed of the waveform.
Phase shift is changing the position in time.
Amplitude is the pitch of the waveform.

"""

# multiplication increases the frequency
expr = t * 12
# division decreases the frequency
expr = t / 12
# addition and subtraction performs a phase shift.
expr = t + 200
expr = t - 200
# negative t will invert the waveform
expr = -t
# modulo changes the amplitude, or volume and pitch by taking the remainder
expr = t % 128  # halve the amplitude
# & (AND) comparison gets two alternative values
expr = t & 128
# | (OR) comparison adds multiple waveforms together.
expr = t | t * 4 | t * 12
# ^ (XOR) comparison does I'm not sure what
expr = t ^ 2
# << and >> (Bitwise) operator shifts more efficiently than + or -, however when used with t, it shifts by octaves.
expr = t >> 1
expr = t << 1
expr = t >> 2
expr = t << 2
# Relational operators (greather than or less than, etc) let you switch sections on and off. See the 16-step sequencer below.
expr = (t > 8000) * t | (t > 16000) * t * 2


# 16-step sequencer
expr = (
    (
        (t % 16000 >= 0 & t % 16000 < 1000) * t
        | (t % 16000 >= 1000 & t % 16000 < 2000) * t * 3
        | (t % 16000 >= 2000 & t % 16000 < 3000) * t * 5
        | (t % 16000 >= 3000 & t % 16000 < 4000) * t * 8
        | (t % 16000 >= 4000 & t % 16000 < 5000) * t * 2
        | (t % 16000 >= 5000 & t % 16000 < 6000) * t
        | (t % 16000 >= 6000 & t % 16000 < 7000) * t * 12
        | (t % 16000 >= 7000 & t % 16000 < 8000) * t * 8
        | (t % 16000 >= 8000 & t % 16000 < 9000) * t * 3
        | (t % 16000 >= 9000 & t % 16000 < 10000) * t
        | (t % 16000 >= 10000 & t % 16000 < 11000) * t * 4
        | (t % 16000 >= 11000 & t % 16000 < 12000) * t * 10
        | (t % 16000 >= 12000 & t % 16000 < 13000) * t * 7
        | (t % 16000 >= 13000 & t % 16000 < 14000) * t * 6
        | (t % 16000 >= 14000 & t % 16000 < 15000) * t * 5
        | (t % 16000 >= 15000 & t % 16000 < 16000) * t * 6
    )
    << (t % 32000 <= 16000)  # transpose up one octave every other run through.
) & 128
