import numpy as np
import time
from collections import deque

import matplotlib.pyplot as plt
from matplotlib import style

style.use("ggplot")

FPS = 125

HM_SECONDS_SLICE = 1 #change seconds if wanted

# plot here any npy file you want from the data directory
data = np.load("../../data/timeSeries/fist_left/1654245921.npy")
# print(len(data))
# plus 1000 to eliminate noise at the start of the recording
for i in range(FPS*HM_SECONDS_SLICE+1000, len(data)):
    new_data = data[i-FPS*HM_SECONDS_SLICE: i]

    c9 = new_data[:, 9]
    # c8 = new_data[:, 8]
    # c10 = new_data[:, 10]

    time.sleep(1/FPS)

    # plt.plot(c8, alpha=1)
    # plt.plot(c10, alpha=1)
    plt.plot(c9, alpha=1)

    # plt.ylim(-3500000, -3380000)
    plt.ylabel("Voltage")
    plt.xlabel("Frames (per second, 120 frames = 1s)")

    # change path if you change the channel
    plt.savefig(f'../../plots/channel9-{HM_SECONDS_SLICE}s-{FPS}hz.png')
    plt.show()

    break
