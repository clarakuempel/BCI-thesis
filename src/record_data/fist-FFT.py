from pylsl import StreamInlet, resolve_stream
import numpy as np
import time
import matplotlib.pyplot as plt
from matplotlib import style
from collections import deque
import os
import random
import tensorflow as tf

ACTION = 'fist_left' # THIS IS THE ACTION THE TEST PERSON IS THINKING!
FFT_MAX_HZ = 60

# can be changed if wanted
HM_SECONDS = 60  # this is approximate. Not 100%. do not depend on this.
TOTAL_ITERS = HM_SECONDS*25  # ~25 iters/sec

last_print = time.time()
fps_counter = deque(maxlen=150)

# first resolve an EEG stream on the lab network
print("looking for an EEG stream...")
# EEG if you stream FFT over an EEG LSL stream in the Oopen BCI Interface
streams1 = resolve_stream('type', 'EEG')
# EEG3 if you stream filtered FFT over an EEG LSL stream in the Oopen BCI Interface
# streams3 = resolve_stream('type', 'EEG3')

fft = StreamInlet(streams1[0])
# fft_filtered = StreamInlet(streams3[0])

print("start: " + ACTION)

channel_datas1 = []
# channel_datas3 = []

for i in range(TOTAL_ITERS):  # how many iterations. Eventually this would be a while True
    channel_data1 = []
    # channel_data3 = []

    for i in range(16): # each of the 16 channels here
        sample1, timestamp = fft.pull_sample()
        # sample3, timestamp = fft_filtered.pull_sample()

        channel_data1.append(sample1[:FFT_MAX_HZ])
        # channel_data3.append(sample3[:FFT_MAX_HZ])

    fps_counter.append(time.time() - last_print)
    last_print = time.time()
    cur_raw_hz = 1/(sum(fps_counter)/len(fps_counter))
    # print(cur_raw_hz)

    channel_datas1.append(channel_data1)
    # channel_datas3.append(channel_data3)

dardirs = ["fft"]
# dardirs = ["fft", "fft_filtered"]
i = 1
for datadir in dardirs:

    if not os.path.exists(datadir):
        os.mkdir(datadir)

    actiondir = f"{datadir}/{ACTION}"
    if not os.path.exists(actiondir):
        os.mkdir(actiondir)

    print(len(channel_datas1))

    print(f"saving {ACTION} data...")

    if i == 1:
        print("one done")
        np.save(os.path.join(actiondir, f"{int(time.time())}.npy"), np.array(channel_datas1))
    else:
        print("two done")
        np.save(os.path.join(actiondir, f"{int(time.time())}.npy"), np.array(channel_datas3))

    i = i + 1
