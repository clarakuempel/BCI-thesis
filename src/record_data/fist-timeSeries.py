"""Example program to show how to read a multi-channel time series from LSL."""
import time
from pylsl import StreamInlet, resolve_stream
from time import sleep
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
from collections import deque
import os
import random

ACTION = 'fist_left' # THIS IS THE ACTION I AM THINKING

# first resolve an EEG stream on the lab network
print("looking for an EEG stream...")
streams = resolve_stream('type', 'EEG2')

# create a new inlet to read from the stream
inlet = StreamInlet(streams[0])

print("start: " + ACTION)

duration = 60

sleep(0)

def testLSLPulseData():
    start = time.time()
    raw_pulse_signals = []

    while time.time() <= start + duration:
        chunk, timestamp = inlet.pull_chunk()
        if timestamp:
            for sample in chunk:
                # print(sample)
                raw_pulse_signals.append(sample)

    return raw_pulse_signals

    # print( "Avg Sampling Rate == {}".format(len(raw_pulse_signals) / duration) )
    # plt.plot([item[0] for item in raw_pulse_signals])
    # plt.ylabel('raw analog signal')
    # plt.show()

raw_pulse_signals = testLSLPulseData()


datadir = "timeSeries"

if not os.path.exists(datadir):
    os.mkdir(datadir)

actiondir = f"{datadir}/{ACTION}"
if not os.path.exists(actiondir):
    os.mkdir(actiondir)

print(f"saving {ACTION} data...")

np.save(os.path.join(actiondir, f"{int(time.time())}.npy"), np.array(raw_pulse_signals))

print("done.")
