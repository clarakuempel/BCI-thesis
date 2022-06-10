import numpy as np
import time
from collections import deque

import matplotlib.pyplot as plt
from matplotlib import style

style.use("ggplot")

FPS = 125
HM_SECONDS_SLICE = 50

# data = np.load("../../data/fft/close_baseline/1654245412.npy")
data = np.load("../../data/timeSeries/fist_left/1654245921.npy")
print(len(data))
# plus 1000 to eliminate noise at the start of the recording
for i in range(FPS*HM_SECONDS_SLICE+1000, len(data)):
    new_data = data[i-FPS*HM_SECONDS_SLICE: i]

    c9 = new_data[:, 9]
    # c9 = new_data[:, 9]
    # c10 = new_data[:, 10]

    time.sleep(1/FPS)

    # plt.plot(c9, alpha=1)
    # plt.plot(c10, alpha=1)
    plt.plot(c9, alpha=1)

    # plt.ylim(-3500000, -3380000)
    plt.ylabel("Voltage")
    plt.xlabel("Frames (per second, 120 frames = 1s)")

    plt.savefig('../../plots/channel9-50s-125hz.png')
    plt.show()

    break
