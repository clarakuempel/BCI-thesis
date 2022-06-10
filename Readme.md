# Studienarbeit from Clara Kümpel

folder explanations:
- data: contains all recorded EEG data as well as a python script for calculating the data's lengths
- models: saved trained models for convolutional neural network 1
- models2: saved trained models for convolutional neural network 2
- plots: saved plots for the written thesis
- src: all source code for the BCI

## Installation / Requirements

To be able to run all python scripts, the following python libraries have to be installed (preferable in an virtual environment):
- numpy
- os
- random
- time
- collections
- matplotlib
- pyOpenBCI
- pylsl
- matplotlib
- collections
- cv2
- tensorflow
- keras

## Scripts that can only be executed with a connected EEG
### print raw EEG signals
To print the raw EEG signals, the EEG has to be connected via the USB. Therefore the user has to specify the correct port.
> $ python  src/setup/print-data-stream.py

### print frame rate    
The user has to specify the correct port.  
> $ python  src/setup/print-frame-rate.py


### receive LSL stream from Open BCI GUI
The stream has to be started in the Open BCI Interface!
> $ python  src/setup/receive-stream.py


### record data
There are 3 options to record data with a started LSL stream.
(instructions for starting the stream and important code segments is given in the thesis)

1. record FFT data
> $ python  src/record_data/fist-FFT.py

2. record TimeSeries data
> $ python  src/record_data/fist-timeSeries.py

3. record while traning a model
> $ python  src/record_data/make-first-data-visual.py


## Scripts that can be executed without a connected EEG

### Plot channels
> $ python src/setup/plot_channels.py

### Train model
> $ python  src/classification/trainingI.py

> $ python  src/classification/trainingII.py

> $ python  src/classification/making-data-and-training.py


### Analysis
To run an analysis of the model you have to specify the following in the analysis.py file:
> $ python  src/analysis/analysis.py


1. model_name
- e.g. "new_models/44.13-acc-64x3-batch-norm-8epoch-1648078391-loss-5.1.model"
2. validation data directoy VALDIR
- e.g. "data/thinking/validation_data"

All accuracies will be saved to the accuracy csv file
