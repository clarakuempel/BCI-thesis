import tensorflow as tf
import numpy as np
import os
import pandas as pd
import matplotlib.pyplot as plt

# best models
# thinking:
# "../../models/thinking/43.47-acc-64x3-batch-norm-1epoch-1654867131-loss-1.61.model"
# "../../models/thinking/43.93-acc-64-128x2-64x2-7epoch-1654865227-loss-3.32.model"
# "../../models2/thinking/41.8-acc-64x3-batch-norm-0epoch-1654866858-loss-1.36.model"
# "../../models2/thinking/41.15-acc-64x3-batch-norm-4epoch-1654867426-loss-2.5.model"

# fft data fist:
# "../../models/fist_fft/5.33-acc-64-128x2-64x2-1epoch-1654866027-loss-47.19.model"
# "../../models/fist_fft/3.33-acc-64-128x2-64x2-4epoch-1654866061-loss-31.39.model"
# "../../models2/fist_fft/23.73-acc-64x3-batch-norm-0epoch-1654865097-loss-66.5.model"

# fft data fist filtered:
# "../../models/fist_fft_filtered/4.22-acc-64-128x2-64x2-3epoch-1654865785-loss-21.62.model"
# "../../models2/fist_fft_filtered/17.38-acc-64x3-batch-norm-7epoch-1654865519-loss-91.25.model"


# others: fist_fft, fist_fft_filtered, thinking
type = "thinking"
MODEL_NAME ="../../models2/fist_fft_filtered/17.38-acc-64x3-batch-norm-7epoch-1654865519-loss-91.25.model"

VALDIR = f'../../data/{type}/validation_data'

CLIP = True  # if your model was trained with np.clip to clip  values
CLIP_VAL = 10  # if above, what was the value +/-

model = tf.keras.models.load_model(MODEL_NAME)


ACTIONS = ['left','none','right']
PRED_BATCH = 32


def get_val_data(valdir, action, batch_size):

    argmax_dict = {0: 0, 1: 0, 2: 0}
    raw_pred_dict = {0: 0, 1: 0, 2: 0}

    action_dir = os.path.join(valdir, action)
    for session_file in os.listdir(action_dir):
        filepath = os.path.join(action_dir,session_file)
        if CLIP:
            data = np.clip(np.load(filepath), -CLIP_VAL, CLIP_VAL) / CLIP_VAL
        else:
            data = np.load(filepath)

        preds = model.predict([data.reshape(-1, 16, 60)], batch_size=batch_size)

        for pred in preds:
            argmax = np.argmax(pred)
            argmax_dict[argmax] += 1
            for idx,value in enumerate(pred):
                raw_pred_dict[idx] += value

    argmax_pct_dict = {}

    for i in argmax_dict:
        total = 0
        correct = argmax_dict[i]
        for ii in argmax_dict:
            total += argmax_dict[ii]

        argmax_pct_dict[i] = round(correct/total, 3)

    return argmax_dict, raw_pred_dict, argmax_pct_dict


def make_conf_mat(left, none, right):

    action_dict = {"left": left, "none": none, "right": right}
    action_conf_mat = pd.DataFrame(action_dict)
    actions = [i for i in action_dict]

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.matshow(action_conf_mat, cmap=plt.cm.RdYlGn)
    ax.set_xticklabels([""]+actions)
    ax.set_yticklabels([""]+actions)

    print("__________")
    print(action_dict)
    for idx, i in enumerate(action_dict):
        print('tf',i)
        for idx2, ii in enumerate(action_dict[i]):
            print(i, ii)
            print(action_dict[i][ii])
            ax.text(idx, idx2, f"{round(float(action_dict[i][ii]),2)}", va='center', ha='center')
    plt.title("Action Thought / Movement")
    plt.ylabel("Predicted Action / Movement")
    plt.savefig(f'../../plots/conf_matrix/{type}.png')
    plt.show()


left_argmax_dict, left_raw_pred_dict, left_argmax_pct_dict = get_val_data(VALDIR, "left", PRED_BATCH)
none_argmax_dict, none_raw_pred_dict, none_argmax_pct_dict = get_val_data(VALDIR, "none", PRED_BATCH)
right_argmax_dict, right_raw_pred_dict, right_argmax_pct_dict = get_val_data(VALDIR, "right", PRED_BATCH)



make_conf_mat(left_argmax_pct_dict, none_argmax_pct_dict, right_argmax_pct_dict)
