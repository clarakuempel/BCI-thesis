import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten
from tensorflow.keras.layers import Conv1D, Conv2D, MaxPooling1D, BatchNormalization, Reshape
from tensorflow.keras import regularizers
import os
import random
import time

DATASEP = 5

# specify the data recording type here (3 options):
datatype = "fist_fft"
# datatype = "fist_fft_filtered"
# datatype = "thinking"

val_starting_dir=f"../../data/{datatype}/validation_data"
train_starting_dir=f"../../data/{datatype}/data"

ACTIONS = ["left", "right", "none"]
reshape = (-1, 16, 60)

def create_data(starting_dir):
    training_data = {}
    for action in ACTIONS:
        if action not in training_data:
            training_data[action] = []

        data_dir = os.path.join(starting_dir,action)
        for item in os.listdir(data_dir):

            data = np.load(os.path.join(data_dir, item))

            for idx, item in enumerate(data):
            	if idx % DATASEP == 0:
                	training_data[action].append(item)

    lengths = [len(training_data[action]) for action in ACTIONS]
    print(lengths)

    for action in ACTIONS:
        np.random.shuffle(training_data[action])
        training_data[action] = training_data[action][:min(lengths)]

    lengths = [len(training_data[action]) for action in ACTIONS]
    print(lengths)
    # creating X, y
    combined_data = []
    for action in ACTIONS:
        for data in training_data[action]:

            if action == "left":
                combined_data.append([data, [1, 0, 0]])

            elif action == "right":
                combined_data.append([data, [0, 0, 1]])

            elif action == "none":
                combined_data.append([data, [0, 1, 0]])

    np.random.shuffle(combined_data)
    print("length:",len(combined_data))
    return combined_data

print("creating training data")
traindata = create_data(starting_dir=train_starting_dir) # here
train_X = []
train_y = []
for X, y in traindata:
    train_X.append(X)
    train_y.append(y)



print("creating testing data")
testdata = create_data(starting_dir=val_starting_dir) # here
test_X = []
test_y = []
for X, y in testdata:
    test_X.append(X)
    test_y.append(y)

print(len(train_X))
print(len(test_X))


print(np.array(train_X).shape)
# train_X = np.array(train_X).reshape(reshape)
# test_X = np.array(test_X).reshape(reshape)

train_X = np.clip(np.array(train_X).reshape(reshape) - np.mean(train_X), -10, 10) / 10
test_X = np.clip(np.array(test_X).reshape(reshape) - np.mean(test_X), -10, 10) / 10


train_y = np.array(train_y)
test_y = np.array(test_y)

model = Sequential()

model.add(Conv1D(64, (5), padding='same', input_shape=train_X.shape[1:]))
model.add(Activation('relu'))

model.add(Conv1D(128, (5), padding='same'))
model.add(Activation('relu'))

model.add(Conv1D(256, (5), padding='same'))
model.add(Activation('relu'))

model.add(Conv1D(512, (5), padding='same'))
model.add(Activation('relu'))

model.add(Conv1D(3, (16)))
model.add(Reshape((3,)))
model.add(Activation('softmax'))

model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

model.summary()

epochs = 10
batch_size = 32
for epoch in range(epochs):
    model.fit(train_X, train_y, batch_size=batch_size, epochs=1, validation_data=(test_X, test_y))
    score = model.evaluate(test_X, test_y, batch_size=batch_size)
    #print(score)
    MODEL_NAME = f"../../models/{datatype}/{round(score[1]*100,2)}-acc-64-128x2-64x2-{epoch}epoch-{int(time.time())}-loss-{round(score[0],2)}.model"
    model.save(MODEL_NAME)
print("saved:")
print(MODEL_NAME)
