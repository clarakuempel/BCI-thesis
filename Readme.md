# Project thesis 2022 for course of Computer Science at DHBW
***by Clara Kümpel***  

topic: Classification of hand movements in human brain activity by a brain computer interface with electroencephalography on the basis of a prototypical implementation

directories explained:
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

### Train model while recording new data
Therefore the user has to specify a model that already exists in the code. (for thinking data) Then the user can record new EEG data while training a model. The model will be updated and the user can see how the model performed.
> $ python  src/classification/making-data-and-training.py


## Scripts that can be executed without a connected EEG

### Plot channels
Run the command. (If wanted, it is possible to specify channels or source files, see code for instructions inside)
> $ python src/setup/plot_channels.py

### Train model
There are two models that can be trained.
1. Train the first neural network on a specified data directory (see code for instructions)
> $ python  src/classification/trainingI.py

The output model is saved in the models directory.

2. Train the second neural network on a specified data directory (see code for instructions)
> $ python  src/classification/trainingII.py  

The output model is saved in the models2 directory.

### Analysis
To run an analysis of the model you have to specify the following in the analysis.py file:
1. type: "thinking" / "fist_fft" / "fist_fft_filtered"
2. model name and location: e.g.  
MODEL_NAME ="../../models2/fist_fft_filtered/17.38-acc-64x3-batch-norm-7epoch-1654865519-loss-91.25.model"  
The best models are saved in the code  
> $ python  src/analysis/analysis.py

A confusion matrix will be plotted.
