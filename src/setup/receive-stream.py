from pylsl import StreamInlet, resolve_stream
import numpy as np
import time
import matplotlib.pyplot as plt
from matplotlib import style
from collections import deque

# this script works for FFT data!

last_print = time.time()
fps_counter = deque(maxlen=150)
# change duration if wanted
duration = 10

print("looking for an EEG stream...")
streams = resolve_stream('type', 'EEG')

inlet = StreamInlet(streams[0])

channel_data = {}

for i in range(duration):  # how many iterations, this could also be a while(True) loop

    for i in range(16): # each of the 16 channels here, with 125 data points
        sample, timestamp = inlet.pull_sample()
        if i not in channel_data:
            channel_data[i] = sample
        else:
            channel_data[i].append(sample)

    fps_counter.append(time.time() - last_print)
    last_print = time.time()
    cur_raw_hz = 1/(sum(fps_counter)/len(fps_counter))
    print(cur_raw_hz)

for chan in channel_data:
    plt.plot(channel_data[chan][:60]) # cut at 60Hz
plt.show()
