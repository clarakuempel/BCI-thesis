from pyOpenBCI import OpenBCICyton
import numpy as np

def print_raw(sample):
    print(sample.channels_data)
    file_object.write(str(sample.channels_data))

# specify own USB port here:
board = OpenBCICyton(port='/dev/tty.usbserial-DM03H72A', daisy=True)
board.start_stream(print_raw)

file_object.close()
