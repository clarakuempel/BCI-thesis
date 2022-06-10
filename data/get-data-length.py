import numpy as np
import os
import random
import time


ACTIONS = ["left", "right", "none"]
starting_dir="thinking/validation_data"

training_data = {}
for action in ACTIONS:
    print(action)
    if action not in training_data:
        training_data[action] = []

    data_dir = os.path.join(starting_dir,action)
    for item in os.listdir(data_dir):
        #print(action, item)
        data = np.load(os.path.join(data_dir, item))

        for item in data:
            training_data[action].append(item)

lengths = [len(training_data[action]) for action in ACTIONS]
print(lengths)
