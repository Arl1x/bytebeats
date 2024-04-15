#!/usr/bin/python3
import math
import pyaudio
import pydub


def create_sound_data(expr):
    assert type(expr) in (
        float,
        int,
    ), f"Expression is not a float or int. Expr: {type(expr)}"
    return chr(int(expr) % 256)


def create_PyAudio(sample_width=1, channels=1, rate=8000, output=True):
    assert isinstance(
        sample_width, int
    ), "Sample_width is not an integer. Defaults to 1."
    assert isinstance(channels, int), "Channels is not an integer. Defaults to 1."
    assert isinstance(rate, int), "Rate is not an integer. Defaults to 8000hz."
    assert isinstance(output, bool), "Output is not a boolean. Defaults to True."

    pa = pyaudio.PyAudio()
    pa_format = pa.get_format_from_width(sample_width)
    return pa.open(format=pa_format, channels=channels, rate=rate, output=output)


def create_AudioSegment(data, sample_width=1, channels=1, frame_rate=8000):
    assert isinstance(
        data, (str, int, float)
    ), f"Data is not a valid string, int, float type. Data: {type(data)}"

    return pydub.AudioSegment(
        bytes(data, "utf-8"),
        sample_width=sample_width,
        channels=channels,
        frame_rate=frame_rate,
    )


def raise_volume(audiosegment, dB):
    assert type(audiosegment) == pydub.AudioSegment, "Not a valid AudioSegment."
    assert isinstance(dB, (int, float)), "dB is not a valid int or float."

    return audiosegment - dB


def lower_volume(audiosegment, dB):
    assert type(audiosegment) == pydub.AudioSegment, "Not a valid AudioSegment."
    assert isinstance(dB, (int, float)), "dB is not a valid int or float."

    return audiosegment + dB
