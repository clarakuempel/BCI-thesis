from pyOpenBCI import OpenBCICyton
from pylsl import StreamInfo, StreamOutlet
import numpy as np

# Because channels_data is the raw data in counts read by the board -> multiply data by a scale factor
# specific scale factor for each board:

# to convert channels_data to uVolts = uVolts per count
SCALE_FACTOR_EEG = (4500000)/24/(2**23-1) #uV/count

SCALE_FACTOR_AUX = 0.002 / (2**4)

print("Creating LSL stream for EEG. \nName: OpenBCIEEG\nID: OpenBCItestEEG\n")
info_eeg = StreamInfo('OpenBCIEEG', 'EEG', 16, 250, 'float32', 'OpenBCItestEEG')
outlet_eeg = StreamOutlet(info_eeg)

print("Creating LSL stream for AUX. \nName: OpenBCIAUX\nID: OpenBCItestEEG\n")
info_aux = StreamInfo('OpenBCIAUX', 'AUX', 3, 250, 'float32', 'OpenBCItestAUX')
outlet_aux = StreamOutlet(info_aux)

data = []
def lsl_streamers(sample):
    outlet_eeg.push_sample(np.array(sample.channels_data)*SCALE_FACTOR_EEG)
    outlet_aux.push_sample(np.array(sample.aux_data)*SCALE_FACTOR_AUX)

board = OpenBCICyton(port='/dev/tty.usbserial-DM03H72A', daisy=True)
board.start_stream(lsl_streamers)
