from pyOpenBCI import OpenBCICyton
import numpy as np
from collections import deque
import time

last_print = time.time()
fps_counter = deque(maxlen=50)
sequence = np.zeros((100, 16))
counter = 0

# connect Open BCI EEG here, specify the needed USB port
board = OpenBCICyton(port='/dev/tty.usbserial-DM03H72A', daisy=True)

def print_raw(sample):
    global last_print
    global sequence
    global counter
    sequence = np.roll(sequence, 1, 0)
    sequence[0, ...] = sample.channels_data

    fps_counter.append(time.time() - last_print)
    last_print = time.time()
    # to show the frame rate (Hz)
    print(f'FPS: {1/(sum(fps_counter)/len(fps_counter)):.2f}, : {len(sequence)}, ... {counter}')

# start stream
board.start_stream(print_raw)
